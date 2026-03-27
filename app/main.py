from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

from app.routers.task_router import task_router
from app.routers.user_router import user_router
from app.core.config import settings, debug_config
from app.core.logging_config import setup_logging


setup_logging()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    if settings.ENV == "dev":
        debug_config()

    yield  # app runs here

    # Shutdown (optional)
    print("App shutting down...")


app = FastAPI(
    title=settings.APP_NAME,
    lifespan=lifespan
)

# CORS CONFIG (IMPORTANT)
origins = [
    "http://localhost:3000",
    "http://localhost:5173",
    "https://fastapi-task-manager-iota.vercel.app/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# include routers
app.include_router(task_router)
app.include_router(user_router)


@app.get("/health", tags=["Health"])
def health():
    return {"status": "ok"}