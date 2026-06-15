"""Analytics service (E-10). Aggregates for the coordination/director dashboard."""
from __future__ import annotations

from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models import (
    Activity,
    Attendance,
    ESTADO_PUBLICADA,
    Enrollment,
    ENROLL_INSCRIPTO,
    SurveyResponse,
)


def overview(db: Session) -> dict:
    publicadas = db.query(Activity).filter(Activity.estado == ESTADO_PUBLICADA).count()
    inscripciones = db.query(Enrollment).filter(Enrollment.estado == ENROLL_INSCRIPTO).count()
    asistencias = db.query(Attendance).count()
    rate = round(asistencias / inscripciones * 100, 1) if inscripciones else 0.0
    return {
        "actividades_publicadas": publicadas,
        "inscripciones": inscripciones,
        "asistencias": asistencias,
        "attendance_rate": rate,
    }


def top_activities(db: Session, limit: int = 5) -> list[dict]:
    rows = (
        db.query(Activity.titulo, func.count(Enrollment.id).label("n"))
        .join(Enrollment, Enrollment.activity_id == Activity.id)
        .filter(Enrollment.estado == ENROLL_INSCRIPTO)
        .group_by(Activity.id, Activity.titulo)
        .order_by(func.count(Enrollment.id).desc())
        .limit(limit)
        .all()
    )
    return [{"titulo": r[0], "inscriptos": int(r[1])} for r in rows]


def attendance_per_activity(db: Session) -> list[dict]:
    """Published activities that have at least one enrollment (skip empty/draft ones)."""
    result = []
    activities = (
        db.query(Activity)
        .filter(Activity.estado == ESTADO_PUBLICADA)
        .order_by(Activity.fecha_inicio.desc())
        .all()
    )
    for a in activities:
        insc = (
            db.query(Enrollment)
            .filter(Enrollment.activity_id == a.id, Enrollment.estado == ENROLL_INSCRIPTO)
            .count()
        )
        if insc == 0:
            continue
        asis = db.query(Attendance).filter(Attendance.activity_id == a.id).count()
        result.append(
            {
                "titulo": a.titulo,
                "inscriptos": insc,
                "asistencias": asis,
                "rate": round(asis / insc * 100, 1) if insc else 0.0,
            }
        )
    return result


def survey_averages(db: Session) -> list[dict]:
    rows = (
        db.query(
            Activity.titulo,
            func.avg(SurveyResponse.rating).label("avg"),
            func.count(SurveyResponse.id).label("n"),
        )
        .join(SurveyResponse, SurveyResponse.activity_id == Activity.id)
        .group_by(Activity.id, Activity.titulo)
        .order_by(func.avg(SurveyResponse.rating).desc())
        .all()
    )
    return [
        {"titulo": r[0], "promedio": round(float(r[1]), 2), "respuestas": int(r[2])}
        for r in rows
    ]
