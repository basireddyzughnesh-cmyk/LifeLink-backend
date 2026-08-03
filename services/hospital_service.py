from sqlalchemy.orm import Session

from models.hospital_model import Hospital

from schemas.hospital_schema import (
    HospitalCreate,
    HospitalUpdate
)


# =========================
# CREATE HOSPITAL
# =========================
def create_hospital(
    hospital: HospitalCreate,
    db: Session
):

    new_hospital = Hospital(
        name=hospital.name,
        location=hospital.location,
        phone=hospital.phone,
        total_beds=hospital.total_beds,
        available_beds=hospital.available_beds,
        emergency_available=hospital.emergency_available
    )

    db.add(new_hospital)
    db.commit()
    db.refresh(new_hospital)

    return new_hospital


# =========================
# GET ALL HOSPITALS
# =========================
def get_all_hospitals(
    db: Session
):

    return db.query(Hospital).all()


# =========================
# GET HOSPITAL BY ID
# =========================
def get_hospital_by_id(
    hospital_id: int,
    db: Session
):

    return (
        db.query(Hospital)
        .filter(Hospital.id == hospital_id)
        .first()
    )


# =========================
# UPDATE HOSPITAL
# =========================
def update_hospital(
    hospital_id: int,
    hospital: HospitalUpdate,
    db: Session
):

    existing_hospital = get_hospital_by_id(
        hospital_id,
        db
    )

    if existing_hospital is None:
        return None


    if hospital.location is not None:
        existing_hospital.location = hospital.location

    if hospital.phone is not None:
        existing_hospital.phone = hospital.phone

    if hospital.total_beds is not None:
        existing_hospital.total_beds = hospital.total_beds

    if hospital.available_beds is not None:
        existing_hospital.available_beds = hospital.available_beds

    if hospital.emergency_available is not None:
        existing_hospital.emergency_available = hospital.emergency_available


    db.commit()
    db.refresh(existing_hospital)

    return existing_hospital


# =========================
# DELETE HOSPITAL
# =========================
def delete_hospital(
    hospital_id: int,
    db: Session
):

    hospital = get_hospital_by_id(
        hospital_id,
        db
    )

    if hospital is None:
        return None

    db.delete(hospital)
    db.commit()

    return hospital


# =========================
# SEARCH HOSPITAL BY LOCATION
# =========================
def search_hospital_by_location(
    location: str,
    db: Session
):

    return (
        db.query(Hospital)
        .filter(
            Hospital.location.ilike(f"%{location}%")
        )
        .all()
    )