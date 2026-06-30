"""
Application to configure logging
"""
import logging
from app.core.config import settings

def configure_logging() -> None:

    log_level = logging.debug if settings.debug else logging.INFO

    logging.basicConfig(
        level = log_level,
        format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",

    )

