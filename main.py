from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import traceback

from database.base import Base
from database.connection import engine

# Models
from models.user_model import User
from models.patient_model import Patient
from models.hospital_model import Hospital
from models.ambulance_model import Ambulance
from models.emergency_model import EmergencyRequest

# Routes
from routes.auth_routes import router as auth_router
from routes.patient_routes import router as patient_router
from routes.hospital_routes import router as hospital_router
from routes.ambulance_routes import router as ambulance_router
from routes.emergency_routes import router as emergency_router
from routes.dashboard_routes import router as dashboard_router   # <-- ADD THIS

# Create Database Tables
Base.metadata.create_all(bind=engine)

# FastAPI App
app = FastAPI(
    title="LifeLink API",
    description="Smart Emergency Ambulance Tracking and Hospital Coordination System",
    version="1.0"
)

# Global Exception Handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    traceback.print_exc()
    return JSONResponse(
        status_code=500,
        content={"error": str(exc)}
    )

# Include Routers
app.include_router(auth_router)
app.include_router(patient_router)
app.include_router(hospital_router)
app.include_router(ambulance_router)
app.include_router(emergency_router)
app.include_router(dashboard_router)   # <-- ADD THIS

# Home Route
@app.get("/")
def home():
    return {
        "message": "LifeLink Backend Running Successfully"
    }