"""Activity catalogue service (E-02 discovery, E-08 admin CRUD)."""
from __future__ import annotations

from datetime import datetime

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.models import (
    Activity,
    ESTADO_PUBLICADA,
    Enrollment,
    ENROLL_INSCRIPTO,
)


def get(db: Session, activity_id: int) -> Activity | None:
    return db.get(Activity, activity_id)


def inscriptos_count(db: Session, activity_id: int) -> int:
    return (
        db.query(Enrollment)
        .filter(Enrollment.activity_id == activity_id, Enrollment.estado == ENROLL_INSCRIPTO)
        .count()
    )


def cupo_info(db: Session, activity: Activity) -> dict:
    taken = inscriptos_count(db, activity.id)
    return {
        "taken": taken,
        "free": max(activity.cupo_max - taken, 0),
        "full": taken >= activity.cupo_max,
    }


def list_published(
    db: Session,
    *,
    tipo: str | None = None,
    fecha: str | None = None,
    min_creditos: int | None = None,
    solo_disponibles: bool = False,
) -> list[Activity]:
    stmt = select(Activity).where(Activity.estado == ESTADO_PUBLICADA)
    if tipo:
        stmt = stmt.where(Activity.tipo == tipo)
    if min_creditos:
        stmt = stmt.where(Activity.creditos >= min_creditos)
    if fecha:
        try:
            day = datetime.fromisoformat(fecha).date()
            stmt = stmt.where(func.date(Activity.fecha_inicio) == day)
        except ValueError:
            pass
    stmt = stmt.order_by(Activity.fecha_inicio.asc())
    activities = list(db.execute(stmt).scalars().all())
    if solo_disponibles:
        activities = [a for a in activities if not cupo_info(db, a)["full"]]
    return activities


def list_all(db: Session) -> list[Activity]:
    return list(
        db.execute(select(Activity).order_by(Activity.fecha_inicio.desc())).scalars().all()
    )


def create(db: Session, **fields) -> Activity:
    activity = Activity(**fields)
    db.add(activity)
    db.commit()
    db.refresh(activity)
    return activity


def update(db: Session, activity: Activity, **fields) -> Activity:
    for key, value in fields.items():
        setattr(activity, key, value)
    db.commit()
    db.refresh(activity)
    return activity
