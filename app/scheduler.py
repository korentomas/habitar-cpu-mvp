"""APScheduler job: email a reminder 24h before each activity (E-04, US-14)."""
from __future__ import annotations

import logging
from datetime import datetime, timedelta, timezone

from apscheduler.schedulers.background import BackgroundScheduler

from app.database import SessionLocal
from app.email_util import send_email
from app.models import (
    Activity,
    ESTADO_PUBLICADA,
    Enrollment,
    ENROLL_INSCRIPTO,
    Notification,
)

logger = logging.getLogger("habitar.scheduler")
scheduler = BackgroundScheduler(timezone="UTC")


def send_reminders() -> None:
    db = SessionLocal()
    try:
        now = datetime.now(timezone.utc)
        window_start = now + timedelta(hours=23)
        window_end = now + timedelta(hours=25)
        activities = (
            db.query(Activity)
            .filter(
                Activity.estado == ESTADO_PUBLICADA,
                Activity.fecha_inicio >= window_start,
                Activity.fecha_inicio <= window_end,
            )
            .all()
        )
        sent = 0
        for activity in activities:
            enrollments = (
                db.query(Enrollment)
                .filter(
                    Enrollment.activity_id == activity.id,
                    Enrollment.estado == ENROLL_INSCRIPTO,
                    Enrollment.reminded.is_(False),
                )
                .all()
            )
            for enr in enrollments:
                msg = (
                    f"Recordatorio: '{activity.titulo}' comienza el "
                    f"{activity.fecha_inicio.strftime('%d/%m/%Y %H:%M')} en {activity.lugar or 'el campus'}."
                )
                db.add(Notification(user_id=enr.user_id, mensaje=msg))
                if enr.user and enr.user.email:
                    send_email(enr.user.email, "Recordatorio de actividad", msg)
                enr.reminded = True
                sent += 1
        db.commit()
        if sent:
            logger.info("Sent %d activity reminders", sent)
    except Exception as exc:  # noqa: BLE001
        logger.warning("Reminder job failed: %s", exc)
        db.rollback()
    finally:
        db.close()


def start_scheduler() -> None:
    if scheduler.running:
        return
    scheduler.add_job(send_reminders, "interval", hours=1, id="reminders", replace_existing=True)
    scheduler.start()
    logger.info("Reminder scheduler started")
