from sqlalchemy.orm import Session

from models.emergency_model import EmergencyRequest
from models.patient_model import Patient

from schemas.emergency_schema import (
    EmergencyCreate,
    EmergencyUpdate
)


# Convert Emergency Data with Patient Name
def emergency_response_data(emergency):

    return {
        "id": emergency.id,

        "patient_id": emergency.patient_id,
        "patient_name": (
            emergency.patient.name
            if emergency.patient
            else None
        ),

        "hospital_id": emergency.hospital_id,
        "ambulance_id": emergency.ambulance_id,

        "emergency_type": emergency.emergency_type,
        "location": emergency.location,
        "status": emergency.status
    }


# =========================
# CREATE EMERGENCY
# =========================
def create_emergency(
    emergency: EmergencyCreate,
    db: Session
):

    new_emergency = EmergencyRequest(
        patient_id=emergency.patient_id,
        hospital_id=emergency.hospital_id,
        ambulance_id=emergency.ambulance_id,
        emergency_type=emergency.emergency_type,
        location=emergency.location,
        status=emergency.status
    )

    db.add(new_emergency)
    db.commit()
    db.refresh(new_emergency)

    return emergency_response_data(new_emergency)


# =========================
# GET ALL EMERGENCIES
# =========================
def get_all_emergencies(
    db: Session
):

    emergencies = (
        db.query(EmergencyRequest)
        .all()
    )

    return [
        emergency_response_data(emergency)
        for emergency in emergencies
    ]


# =========================
# GET EMERGENCY BY ID
# =========================
def get_emergency_by_id(
    emergency_id: int,
    db: Session
):

    emergency = (
        db.query(EmergencyRequest)
        .filter(
            EmergencyRequest.id == emergency_id
        )
        .first()
    )

    if emergency:
        return emergency_response_data(emergency)

    return None


# =========================
# UPDATE EMERGENCY
# =========================
def update_emergency(
    emergency_id: int,
    emergency_data: EmergencyUpdate,
    db: Session
):

    emergency = (
        db.query(EmergencyRequest)
        .filter(
            EmergencyRequest.id == emergency_id
        )
        .first()
    )

    if emergency:

        if emergency_data.hospital_id is not None:
            emergency.hospital_id = emergency_data.hospital_id

        if emergency_data.ambulance_id is not None:
            emergency.ambulance_id = emergency_data.ambulance_id

        if emergency_data.location is not None:
            emergency.location = emergency_data.location

        if emergency_data.status is not None:
            emergency.status = emergency_data.status

        db.commit()
        db.refresh(emergency)

        return emergency_response_data(emergency)

    return None


# =========================
# DELETE EMERGENCY
# =========================
def delete_emergency(
    emergency_id: int,
    db: Session
):

    emergency = (
        db.query(EmergencyRequest)
        .filter(
            EmergencyRequest.id == emergency_id
        )
        .first()
    )

    if emergency:
        db.delete(emergency)
        db.commit()

    return emergency


# =========================
# SEARCH EMERGENCIES
# =========================
def search_emergencies(
    keyword: str,
    db: Session
):

    emergencies = (
        db.query(EmergencyRequest)
        .join(Patient)
        .filter(
            (EmergencyRequest.emergency_type.ilike(f"%{keyword}%")) |
            (EmergencyRequest.location.ilike(f"%{keyword}%")) |
            (EmergencyRequest.status.ilike(f"%{keyword}%")) |
            (Patient.name.ilike(f"%{keyword}%"))
        )
        .all()
    )

    return [
        emergency_response_data(emergency)
        for emergency in emergencies
    ]