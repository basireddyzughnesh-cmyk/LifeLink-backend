from pydantic import BaseModel


# Create Ambulance Request Schema
class AmbulanceCreate(BaseModel):
    vehicle_number: str
    driver_name: str
    driver_phone: str
    current_location: str
    status: str


# Update Ambulance Request Schema
# Only fields that need changes can be sent
class AmbulanceUpdate(BaseModel):
    current_location: str | None = None
    status: str | None = None


# Response Schema
class AmbulanceResponse(BaseModel):
    id: int
    vehicle_number: str
    driver_name: str
    driver_phone: str
    current_location: str
    status: str

    model_config = {
        "from_attributes": True
    }