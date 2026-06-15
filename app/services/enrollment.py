"""Enrollment service (E-03). Cupo enforced transactionally with a row lock."""
from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import (
    Activity,
    ESTADO_PUBLICADA,
    Enrollment,
    ENROLL_BAJA,
    ENROLL_INSCRIPTO,
)


class EnrollError(Exception):
    pass


def active_enrollment(db: Session, activity_id: int, user_id: int) -> Enrollment | None:
    return (
        db.query(Enrollment)
        .filter(
            Enrollment.activity_id == activity_id,
            Enrollment.user_id == user_id,
            Enrollment.estado == ENROLL_INSCRIPTO,
        )
        .first()
    )


def is_enrolled(db: Session, activity_id: int, user_id: int) -> bool:
    return active_enrollment(db, activity_id, user_id) is not None


def enroll(db: Session, activity_id: int, user_id: int) -> Activity:
    """Atomically enroll a user, respecting cupo. Raises EnrollError on failure."""
    # Lock the activity row so concurrent enrolls serialise on cupo.
    activity = db.execute(
        select(Activity).where(Activity.id == activity_id).with_for_update()
    ).scalar_one_or_none()
    if activity is None:
        raise EnrollError("La actividad no existe.")
    if activity.estado != ESTADO_PUBLICADA:
        raise EnrollError("La actividad no está disponible para inscripción.")

    existing = (
        db.query(Enrollment)
        .filter(Enrollment.activity_id == activity_id, Enrollment.user_id == user_id)
        .first()
    )
    if existing and existing.estado == ENROLL_INSCRIPTO:
        raise EnrollError("Ya estás inscripto en esta actividad.")

    taken = (
        db.query(Enrollment)
        .filter(Enrollment.activity_id == activity_id, Enrollment.estado == ENROLL_INSCRIPTO)
        .count()
    )
    if taken >= activity.cupo_max:
        db.rollback()
        raise EnrollError("No quedan cupos disponibles.")

    if existing:
        existing.estado = ENROLL_INSCRIPTO
        existing.reminded = False  # re-arm the 24h reminder after a baja/re-inscripción
    else:
        db.add(Enrollment(activity_id=activity_id, user_id=user_id, estado=ENROLL_INSCRIPTO))
    db.commit()
    return activity


def unenroll(db: Session, activity_id: int, user_id: int) -> None:
    enr = active_enrollment(db, activity_id, user_id)
    if not enr:
        raise EnrollError("No estás inscripto en esta actividad.")
    enr.estado = ENROLL_BAJA
    db.commit()


def my_activities(db: Session, user_id: int) -> list[Activity]:
    rows = (
        db.query(Activity)
        .join(Enrollment, Enrollment.activity_id == Activity.id)
        .filter(
            Enrollment.user_id == user_id,
            Enrollment.estado == ENROLL_INSCRIPTO,
            Activity.estado == ESTADO_PUBLICADA,
        )
        .order_by(Activity.fecha_inicio.asc())
        .all()
    )
    return list(rows)


def inscriptos(db: Session, activity_id: int) -> list[Enrollment]:
    return (
        db.query(Enrollment)
        .filter(Enrollment.activity_id == activity_id, Enrollment.estado == ENROLL_INSCRIPTO)
        .all()
    )
