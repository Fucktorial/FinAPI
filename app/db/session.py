from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.core.config import settings

engine = create_engine(settings.db.SQLALCHEMY_DATABASE_URL)


class SessionLocal(Session):
    def __init__(self):
        super().__init__(bind=engine)


def get_db():
    return SessionLocal()