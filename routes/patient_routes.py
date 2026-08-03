from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database.connection import get_db

from schemas.patient_schema import (
    PatientCreate,
    PatientUpdate,
    PatientResponse
)

from services.patient_service import (
    create_patient,
    get_all_patients,
    get_patient_by_id,
    update_patient,
    delete_patient,
    search_patient_by_name
)


router = APIRouter(
    prefix="/patients",
    tags=["Patients"]
)


# =========================
# CREATE PATIENT
# =========================
@router.post(
    "/",
    response_model=PatientResponse,
    status_code=status.HTTP_201_CREATED
)
def add_patient(
    patient: PatientCreate,
    db: Session = Depends(get_db)
):
    return create_patient(
        patient,
        db
    )


# =========================
# GET ALL PATIENTS
# =========================
@router.get(
    "/",
    response_model=list[PatientResponse]
)
def all_patients(
    db: Session = Depends(get_db)
):
    return get_all_patients(db)


# =========================
# SEARCH PATIENT BY NAME
# =========================
@router.get(
    "/search/",
    response_model=list[PatientResponse]
)
def search_patient(
    name: str,
    db: Session = Depends(get_db)
):
    return search_patient_by_name(
        name,
        db
    )


# =========================
# GET PATIENT BY ID
# =========================
@router.get(
    "/{patient_id}",
    response_model=PatientResponse
)
def single_patient(
    patient_id: int,
    db: Session = Depends(get_db)
):

    patient = get_patient_by_id(
        patient_id,
        db
    )

    if patient is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Patient not found"
        )

    return patient


# =========================
# UPDATE PATIENT
# =========================
@router.put(
    "/{patient_id}",
    response_model=PatientResponse
)
def edit_patient(
    patient_id: int,
    patient: PatientUpdate,
    db: Session = Depends(get_db)
):

    updated = update_patient(
        patient_id,
        patient,
        db
    )

    if updated is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Patient not found"
        )

    return updated


# =========================
# DELETE PATIENT
# =========================
@router.delete(
    "/{patient_id}",
    status_code=status.HTTP_200_OK
)
def remove_patient(
    patient_id: int,
    db: Session = Depends(get_db)
):

    deleted = delete_patient(
        patient_id,
        db
    )

    if deleted is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Patient not found"
        )

    return {
        "message": "Patient deleted successfully"
    }