from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database.connection import get_db

from schemas.hospital_schema import (
    HospitalCreate,
    HospitalUpdate,
    HospitalResponse
)

from services.hospital_service import (
    create_hospital,
    get_all_hospitals,
    get_hospital_by_id,
    update_hospital,
    delete_hospital,
    search_hospital_by_location
)


router = APIRouter(
    prefix="/hospitals",
    tags=["Hospitals"]
)


# =========================
# CREATE HOSPITAL
# =========================
@router.post(
    "/",
    response_model=HospitalResponse,
    status_code=status.HTTP_201_CREATED
)
def add_hospital(
    hospital: HospitalCreate,
    db: Session = Depends(get_db)
):
    return create_hospital(
        hospital,
        db
    )


# =========================
# GET ALL HOSPITALS
# =========================
@router.get(
    "/",
    response_model=list[HospitalResponse]
)
def get_hospitals(
    db: Session = Depends(get_db)
):
    return get_all_hospitals(db)


# =========================
# SEARCH HOSPITAL BY LOCATION
# =========================
@router.get(
    "/search/",
    response_model=list[HospitalResponse]
)
def search_hospital(
    location: str,
    db: Session = Depends(get_db)
):
    return search_hospital_by_location(
        location,
        db
    )


# =========================
# GET HOSPITAL BY ID
# =========================
@router.get(
    "/{hospital_id}",
    response_model=HospitalResponse
)
def get_hospital(
    hospital_id: int,
    db: Session = Depends(get_db)
):

    hospital = get_hospital_by_id(
        hospital_id,
        db
    )

    if hospital is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Hospital not found"
        )

    return hospital


# =========================
# UPDATE HOSPITAL
# =========================
@router.put(
    "/{hospital_id}",
    response_model=HospitalResponse
)
def edit_hospital(
    hospital_id: int,
    hospital: HospitalUpdate,
    db: Session = Depends(get_db)
):

    updated = update_hospital(
        hospital_id,
        hospital,
        db
    )

    if updated is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Hospital not found"
        )

    return updated


# =========================
# DELETE HOSPITAL
# =========================
@router.delete(
    "/{hospital_id}",
    status_code=status.HTTP_200_OK
)
def remove_hospital(
    hospital_id: int,
    db: Session = Depends(get_db)
):

    deleted = delete_hospital(
        hospital_id,
        db
    )

    if deleted is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Hospital not found"
        )

    return {
        "message": "Hospital deleted successfully"
    }