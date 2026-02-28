from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    # ===== App =====
    APP_NAME: str = "Note Manager API"
    ENV: str = "dev"
    DEBUG: bool = True

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
        env_file = ".env"
        extra = "ignore"


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()