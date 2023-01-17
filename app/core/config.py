from pydantic import BaseSettings


class DBSettings(BaseSettings):
    SQLALCHEMY_DATABASE_URL: str = "postgresql://Admin:Admin@localhost:5432/fast_api_db"


class Settings(BaseSettings):
    db: DBSettings = DBSettings()



settings = Settings()