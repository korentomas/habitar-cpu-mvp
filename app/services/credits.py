"""Credits & progress service (E-07)."""
from __future__ import annotations

from sqlalchemy import func
from sqlalchemy.orm import Session

from app.config import settings
from app.models import Activity, AppConfig, Attendance


def required_credits(db: Session) -> int:
    row = db.get(AppConfig, "required_credits")
    if row and row.value.isdigit():
        return int(row.value)
    return settings.REQUIRED_CREDITS


def accumulated_credits(db: Session, user_id: int) -> int:
    total = (
        db.query(func.coalesce(func.sum(Activity.creditos), 0))
        .join(Attendance, Attendance.activity_id == Activity.id)
        .filter(Attendance.user_id == user_id)
        .scalar()
    )
    return int(total or 0)


def completed_activities(db: Session, user_id: int) -> list[tuple[Activity, object]]:
    rows = (
        db.query(Activity, Attendance.validated_at)
        .join(Attendance, Attendance.activity_id == Activity.id)
        .filter(Attendance.user_id == user_id)
        .order_by(Attendance.validated_at.desc())
        .all()
    )
    return [(r[0], r[1]) for r in rows]


def progress(db: Session, user_id: int) -> dict:
    acc = accumulated_credits(db, user_id)
    req = required_credits(db)
    pct = min(round(acc / req * 100), 100) if req else 0
    return {"accumulated": acc, "required": req, "pct": pct, "complete": acc >= req}
