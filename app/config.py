"""Application settings loaded from environment / .env."""
import os

from dotenv import load_dotenv

load_dotenv()


def _normalize_db_url(url: str) -> str:
    """Ensure SQLAlchemy uses the psycopg (v3) driver."""
    if not url:
        return url
    if url.startswith("postgres://"):
        url = url.replace("postgres://", "postgresql://", 1)
    if url.startswith("postgresql://"):
        url = url.replace("postgresql://", "postgresql+psycopg://", 1)
    return url


class Settings:
    APP_NAME: str = os.getenv("APP_NAME", "Módulo Habitar")
    DATABASE_URL: str = _normalize_db_url(os.getenv("DATABASE_URL", ""))
    SECRET_KEY: str = os.getenv("SECRET_KEY", "dev-secret-change-me")
    REQUIRED_CREDITS: int = int(os.getenv("REQUIRED_CREDITS", "10"))

    SMTP_HOST: str = os.getenv("SMTP_HOST", "")
    SMTP_PORT: int = int(os.getenv("SMTP_PORT", "587"))
    SMTP_USER: str = os.getenv("SMTP_USER", "")
    SMTP_PASSWORD: str = os.getenv("SMTP_PASSWORD", "")
    SMTP_FROM: str = os.getenv("SMTP_FROM", "Modulo Habitar <no-reply@example.com>")


settings = Settings()
