from fastapi import FastAPI
from app.core.config import settings

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

    return app