from sqlalchemy.orm import Session

from models.patient_model import Patient

from schemas.patient_schema import (
    PatientCreate,
    PatientUpdate
)


# =========================
# CREATE PATIENT
# =========================
def create_patient(
    patient: PatientCreate,
    db: Session
):

    new_patient = Patient(
        name=patient.name,
        age=patient.age,
        gender=patient.gender,
        blood_group=patient.blood_group,
        phone=patient.phone,
        address=patient.address
    )

    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)

    return new_patient


# =========================
# GET ALL PATIENTS
# =========================
def get_all_patients(
    db: Session
):

    return db.query(Patient).all()


# =========================
# GET PATIENT BY ID
# =========================
def get_patient_by_id(
    patient_id: int,
    db: Session
):

    return (
        db.query(Patient)
        .filter(Patient.id == patient_id)
        .first()
    )


# =========================
# UPDATE PATIENT
# =========================
def update_patient(
    patient_id: int,
    patient: PatientUpdate,
    db: Session
):

    existing_patient = get_patient_by_id(
        patient_id,
        db
    )

    if existing_patient is None:
        return None


    if patient.name is not None:
        existing_patient.name = patient.name

    if patient.age is not None:
        existing_patient.age = patient.age

    if patient.gender is not None:
        existing_patient.gender = patient.gender

    if patient.blood_group is not None:
        existing_patient.blood_group = patient.blood_group

    if patient.phone is not None:
        existing_patient.phone = patient.phone

    if patient.address is not None:
        existing_patient.address = patient.address


    db.commit()
    db.refresh(existing_patient)

    return existing_patient


# =========================
# DELETE PATIENT
# =========================
def delete_patient(
    patient_id: int,
    db: Session
):

    patient = get_patient_by_id(
        patient_id,
        db
    )

    if patient is None:
        return None

    db.delete(patient)
    db.commit()

    return patient


# =========================
# SEARCH PATIENT BY NAME
# =========================
def search_patient_by_name(
    name: str,
    db: Session
):

    return (
        db.query(Patient)
        .filter(
            Patient.name.ilike(f"%{name}%")
        )
        .all()
    )