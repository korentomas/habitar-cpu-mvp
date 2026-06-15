"""E-02 Discovery & exploration of activities (student-facing)."""
from __future__ import annotations

from fastapi import APIRouter, Depends, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import TIPO_PRESENCIAL, TIPO_VIRTUAL, User
from app.security import current_user_required
from app.services import activities as activities_svc
from app.services import enrollment as enrollment_svc
from app.templating import render

router = APIRouter()


@router.get("/actividades")
def list_activities(
    request: Request,
    tipo: str = "",
    fecha: str = "",
    min_creditos: str = "",
    solo_disponibles: str = "",
    user: User = Depends(current_user_required),
    db: Session = Depends(get_db),
):
    min_cred = int(min_creditos) if min_creditos.isdigit() else None
    items = activities_svc.list_published(
        db,
        tipo=tipo or None,
        fecha=fecha or None,
        min_creditos=min_cred,
        solo_disponibles=bool(solo_disponibles),
    )
    enrolled_ids = {a.id for a in enrollment_svc.my_activities(db, user.id)}
    rows = [{"a": a, "cupo": activities_svc.cupo_info(db, a), "enrolled": a.id in enrolled_ids} for a in items]
    return render(
        request, "student/actividades.html", user=user, db=db,
        rows=rows,
        filtros={"tipo": tipo, "fecha": fecha, "min_creditos": min_creditos, "solo_disponibles": solo_disponibles},
        tipos=[TIPO_PRESENCIAL, TIPO_VIRTUAL],
    )


@router.get("/actividades/{activity_id}")
def activity_detail(
    request: Request,
    activity_id: int,
    user: User = Depends(current_user_required),
    db: Session = Depends(get_db),
):
    activity = activities_svc.get(db, activity_id)
    if activity is None or activity.estado != "publicada":
        return RedirectResponse(url="/actividades?err=La actividad no está disponible.", status_code=303)
    cupo = activities_svc.cupo_info(db, activity)
    enrolled = enrollment_svc.is_enrolled(db, activity_id, user.id)
    return render(
        request, "student/detalle.html", user=user, db=db,
        a=activity, cupo=cupo, enrolled=enrolled,
    )
