from pydantic import BaseModel


# =========================
# CREATE HOSPITAL
# =========================
class HospitalCreate(BaseModel):
    name: str
    location: str
    phone: str
    total_beds: int
    available_beds: int
    emergency_available: bool


# =========================
# UPDATE HOSPITAL
# =========================
class HospitalUpdate(BaseModel):
    location: str | None = None
    phone: str | None = None
    total_beds: int | None = None
    available_beds: int | None = None
    emergency_available: bool | None = None


# =========================
# RESPONSE HOSPITAL
# =========================
class HospitalResponse(BaseModel):
    id: int
    name: str
    location: str
    phone: str
    total_beds: int
    available_beds: int
    emergency_available: bool

    model_config = {
        "from_attributes": True
    }