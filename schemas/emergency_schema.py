from pydantic import BaseModel


# =========================
# CREATE EMERGENCY
# =========================
class EmergencyCreate(BaseModel):
    patient_id: int
    hospital_id: int
    ambulance_id: int
    emergency_type: str
    location: str
    status: str


# =========================
# UPDATE EMERGENCY
# =========================
class EmergencyUpdate(BaseModel):
    hospital_id: int | None = None
    ambulance_id: int | None = None
    location: str | None = None
    status: str | None = None


# =========================
# RESPONSE EMERGENCY
# =========================
class EmergencyResponse(BaseModel):
    id: int

    patient_id: int
    patient_name: str | None = None

    hospital_id: int
    ambulance_id: int

    emergency_type: str
    location: str
    status: str

    model_config = {
        "from_attributes": True
    }