from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base , Session
from app.core.config import settings
from collections.abc import Generator

#Engine
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True # Detect DB Connections and Auto Reconnect
)

#Session
SessionLocal = sessionmaker(
    autoflush=False,
    autocommit = False,
    bind=engine
)

#Base Model
Base = declarative_base()

#Dependency
def get_db() -> Generator[Session , None , None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
