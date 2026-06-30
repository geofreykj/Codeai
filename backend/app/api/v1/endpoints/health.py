from fastapi import APIRouter
from app.schemas.health import HealthResponse 


router = APIRouter()

@router.get("/", response_model=HealthResponse, summary="Health check", description="Returns the current health status of the application")
async def health_check():
    return HealthResponse(
    status="healthy"
    )
