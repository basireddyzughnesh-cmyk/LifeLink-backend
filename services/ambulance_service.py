from sqlalchemy.orm import Session

from models.ambulance_model import Ambulance
from schemas.ambulance_schema import (
    AmbulanceCreate,
    AmbulanceUpdate
)


# =========================
# CREATE AMBULANCE
# =========================
def create_ambulance(
    ambulance: AmbulanceCreate,
    db: Session
):

    new_ambulance = Ambulance(
        vehicle_number=ambulance.vehicle_number,
        driver_name=ambulance.driver_name,
        driver_phone=ambulance.driver_phone,
        current_location=ambulance.current_location,
        status=ambulance.status
    )

    db.add(new_ambulance)
    db.commit()
    db.refresh(new_ambulance)

    return new_ambulance


# =========================
# GET ALL AMBULANCES
# =========================
def get_all_ambulances(db: Session):

    return db.query(Ambulance).all()


# =========================
# GET AMBULANCE BY ID
# =========================
def get_ambulance_by_id(
    ambulance_id: int,
    db: Session
):

    return (
        db.query(Ambulance)
        .filter(Ambulance.id == ambulance_id)
        .first()
    )


# =========================
# UPDATE AMBULANCE
# =========================
def update_ambulance(
    ambulance_id: int,
    ambulance_data: AmbulanceUpdate,
    db: Session
):

    ambulance = (
        db.query(Ambulance)
        .filter(Ambulance.id == ambulance_id)
        .first()
    )

    if ambulance:

        if ambulance_data.current_location is not None:
            ambulance.current_location = ambulance_data.current_location

        if ambulance_data.status is not None:
            ambulance.status = ambulance_data.status

        db.commit()
        db.refresh(ambulance)

    return ambulance


# =========================
# DELETE AMBULANCE
# =========================
def delete_ambulance(
    ambulance_id: int,
    db: Session
):

    ambulance = (
        db.query(Ambulance)
        .filter(Ambulance.id == ambulance_id)
        .first()
    )

    if ambulance:
        db.delete(ambulance)
        db.commit()

    return ambulance


# =========================
# SEARCH AMBULANCE BY STATUS
# =========================
def search_ambulance_by_status(
    status: str,
    db: Session
):

    return (
        db.query(Ambulance)
        .filter(Ambulance.status.ilike(f"%{status}%"))
        .all()
    )