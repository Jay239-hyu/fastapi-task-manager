import logging
from app.core.config import settings

def setup_logging():

    if settings.LOGGING_OFF:
        logging.disable(logging.CRITICAL)
        return

    level = logging.DEBUG if settings.DEBUG else logging.INFO

    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        force=True,  
    )

    #keep uvicorn in sync
    logging.getLogger("uvicorn.error").setLevel(level)
    logging.getLogger("uvicorn.access").setLevel(level)