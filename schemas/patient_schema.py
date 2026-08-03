from pydantic import BaseModel


# =========================
# CREATE PATIENT
# =========================
class PatientCreate(BaseModel):
    name: str
    age: int
    gender: str
    blood_group: str
    phone: str
    address: str


# =========================
# UPDATE PATIENT
# =========================
class PatientUpdate(BaseModel):
    name: str | None = None
    age: int | None = None
    gender: str | None = None
    blood_group: str | None = None
    phone: str | None = None
    address: str | None = None


# =========================
# RESPONSE PATIENT
# =========================
class PatientResponse(BaseModel):
    id: int
    name: str
    age: int
    gender: str
    blood_group: str
    phone: str
    address: str

    model_config = {
        "from_attributes": True
    }