from fastapi import FastAPI
from app.routers.task_router import task_router
from app.core.config import settings
from app.routers.user_router import user_router
from app.core.logging_config import setup_logging


setup_logging()


app = FastAPI(title=settings.APP_NAME)


# include routers
app.include_router(task_router)
app.include_router(user_router)

@app.get("/health" , tags=["Health"])
def health():
    return {"status": "ok"}

