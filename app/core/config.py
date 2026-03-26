from pydantic_settings import BaseSettings
from functools import lru_cache
import os

class Settings(BaseSettings):
    # ===== App =====
    APP_NAME: str = "Note Manager API"
    ENV: str = "dev"
    DEBUG: bool = False   #safe default

    # ===== Database =====
    DATABASE_URL: str

    # ===== CORS =====
    ALLOWED_ORIGINS: list[str] = ["*"] 

    # ===== Auth =====
    SECRET_KEY : str
    ALGORITHM : str
    EXP_TIME_IN_SEC : int

    # ===== Logging ====
    LOGGING_OFF : bool = False

    class Config:
        env_file = f".env.{os.getenv('ENV', 'dev')}"
        extra = "ignore"


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()


def debug_config():
    print(f"ENV: {settings.ENV}")
    print(f"DEBUG: {settings.DEBUG}")