from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database.connection import get_db

from schemas.ambulance_schema import (
    AmbulanceCreate,
    AmbulanceResponse,
    AmbulanceUpdate
)

from services.ambulance_service import (
    create_ambulance,
    get_all_ambulances,
    get_ambulance_by_id,
    update_ambulance,
    delete_ambulance,
    search_ambulance_by_status
)


router = APIRouter(
    prefix="/ambulances",
    tags=["Ambulances"]
)


# =========================
# CREATE AMBULANCE
# =========================
@router.post(
    "/",
    response_model=AmbulanceResponse,
    status_code=status.HTTP_201_CREATED
)
def add_ambulance(
    ambulance: AmbulanceCreate,
    db: Session = Depends(get_db)
):
    return create_ambulance(
        ambulance,
        db
    )


# =========================
# GET ALL AMBULANCES
# =========================
@router.get(
    "/",
    response_model=list[AmbulanceResponse]
)
def get_ambulances(
    db: Session = Depends(get_db)
):
    return get_all_ambulances(db)


# =========================
# SEARCH AMBULANCE BY STATUS
# =========================
@router.get(
    "/search/",
    response_model=list[AmbulanceResponse]
)
def search_ambulance(
    status: str,
    db: Session = Depends(get_db)
):
    return search_ambulance_by_status(
        status,
        db
    )


# =========================
# GET AMBULANCE BY ID
# =========================
@router.get(
    "/{ambulance_id}",
    response_model=AmbulanceResponse
)
def get_ambulance(
    ambulance_id: int,
    db: Session = Depends(get_db)
):

    ambulance = get_ambulance_by_id(
        ambulance_id,
        db
    )

    if ambulance is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ambulance not found"
        )

    return ambulance


# =========================
# UPDATE AMBULANCE
# =========================
@router.put(
    "/{ambulance_id}",
    response_model=AmbulanceResponse
)
def update_ambulance_data(
    ambulance_id: int,
    ambulance: AmbulanceUpdate,
    db: Session = Depends(get_db)
):

    updated = update_ambulance(
        ambulance_id,
        ambulance,
        db
    )

    if updated is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ambulance not found"
        )

    return updated


# =========================
# DELETE AMBULANCE
# =========================
@router.delete(
    "/{ambulance_id}",
    status_code=status.HTTP_200_OK
)
def delete_ambulance_data(
    ambulance_id: int,
    db: Session = Depends(get_db)
):

    deleted = delete_ambulance(
        ambulance_id,
        db
    )

    if deleted is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ambulance not found"
        )

    return {
        "message": "Ambulance deleted successfully"
    }