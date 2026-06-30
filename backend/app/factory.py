from fastapi import FastAPI
from app.core.config import settings
from app.api.v1.router import router as api_router
from app.core.logging import configure_logging
import logging


def create_application() -> FastAPI:
    """
    Create and configure the FastAPI application instance.

    Returns:
        FastAPI: Configured application instance.
    """
    app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        description=settings.app_description
    )
    
    configure_logging()
    logger = logging.getLogger(__name__)
    logger.info("Creating FastAPI application...")

    logger.info("Registering API routes...")
    app.include_router(api_router, prefix="/api/v1")
    logger.info("Application initialized successfully.")

    return app