"""FastAPI application entrypoint for the Módulo Habitar platform."""
from __future__ import annotations

import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware

from app.config import settings
from app.database import Base, SessionLocal, engine
from app.models import (
    ROLE_COORDINACION,
    ROLE_DIRECTOR,
    ROLE_DOCENTE,
)
from app.routers import (
    admin_activities,
    admin_enroll,
    analytics,
    attendance,
    auth,
    discovery,
    enrollment,
    faq,
)
from app.scheduler import start_scheduler
from app.security import NotAuthenticated, NotAuthorized, get_current_user
from app.seed import seed_all
from app.templating import render

logging.basicConfig(level=logging.INFO)


@asynccontextmanager
async def lifespan(_app: FastAPI):
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        seed_all(db)
    finally:
        db.close()
    start_scheduler()
    yield


app = FastAPI(title=settings.APP_NAME, lifespan=lifespan)
app.add_middleware(SessionMiddleware, secret_key=settings.SECRET_KEY, max_age=60 * 60 * 24 * 7)
app.mount("/static", StaticFiles(directory="app/static"), name="static")


# ---- Auth control-flow -> friendly redirects -------------------------------
@app.exception_handler(NotAuthenticated)
async def _not_authenticated(request: Request, _exc: NotAuthenticated):
    return RedirectResponse(url="/login", status_code=303)


@app.exception_handler(NotAuthorized)
async def _not_authorized(request: Request, _exc: NotAuthorized):
    return render(request, "errors/403.html", status_code=403)


# ---- Routers ----------------------------------------------------------------
app.include_router(auth.router)
app.include_router(discovery.router)
app.include_router(enrollment.router)
app.include_router(attendance.router)
app.include_router(admin_activities.router)
app.include_router(admin_enroll.router)
app.include_router(analytics.router)
app.include_router(faq.router)


@app.get("/healthz")
async def healthz():
    return {"status": "ok"}


@app.get("/")
async def root(request: Request):
    db = SessionLocal()
    try:
        user = get_current_user(request, db)
    finally:
        db.close()
    if user is None:
        return RedirectResponse(url="/login", status_code=303)
    if user.role == ROLE_COORDINACION:
        return RedirectResponse(url="/admin", status_code=303)
    if user.role == ROLE_DOCENTE:
        return RedirectResponse(url="/docente", status_code=303)
    if user.role == ROLE_DIRECTOR:
        return RedirectResponse(url="/analytics", status_code=303)
    return RedirectResponse(url="/home", status_code=303)
