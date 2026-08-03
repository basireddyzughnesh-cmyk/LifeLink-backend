from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database.connection import get_db

from schemas.emergency_schema import (
    EmergencyCreate,
    EmergencyUpdate,
    EmergencyResponse
)

from services.emergency_service import (
    create_emergency,
    get_all_emergencies,
    get_emergency_by_id,
    update_emergency,
    delete_emergency,
    search_emergencies
)

from security.dependencies import get_current_user
from models.user_model import User


router = APIRouter(
    prefix="/emergencies",
    tags=["Emergencies"]
)


# =========================
# CREATE EMERGENCY
# =========================
@router.post(
    "/",
    response_model=EmergencyResponse,
    status_code=status.HTTP_201_CREATED
)
def add_emergency(
    emergency: EmergencyCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return create_emergency(
        emergency,
        db
    )


# =========================
# GET ALL EMERGENCIES
# =========================
@router.get(
    "/",
    response_model=list[EmergencyResponse]
)
def get_emergencies(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return get_all_emergencies(db)


# =========================
# SEARCH EMERGENCIES
# =========================
@router.get(
    "/search",
    response_model=list[EmergencyResponse]
)
def search_emergency_data(
    keyword: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return search_emergencies(
        keyword,
        db
    )


# =========================
# GET EMERGENCY BY ID
# =========================
@router.get(
    "/{emergency_id}",
    response_model=EmergencyResponse
)
def get_emergency(
    emergency_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    emergency = get_emergency_by_id(
        emergency_id,
        db
    )

    if emergency is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Emergency request not found"
        )

    return emergency


# =========================
# UPDATE EMERGENCY
# =========================
@router.put(
    "/{emergency_id}",
    response_model=EmergencyResponse
)
def update_emergency_data(
    emergency_id: int,
    emergency: EmergencyUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    updated = update_emergency(
        emergency_id,
        emergency,
        db
    )

    if updated is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Emergency request not found"
        )

    return updated


# =========================
# DELETE EMERGENCY
# =========================
@router.delete(
    "/{emergency_id}"
)
def delete_emergency_data(
    emergency_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    deleted = delete_emergency(
        emergency_id,
        db
    )

    if deleted is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Emergency request not found"
        )

    return {
        "message": "Emergency request deleted successfully"
    }