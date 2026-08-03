from sqlalchemy.orm import Session

from models.patient_model import Patient
from models.hospital_model import Hospital
from models.ambulance_model import Ambulance
from models.emergency_model import EmergencyRequest


def get_dashboard_data(db: Session):

    total_patients = db.query(Patient).count()

    total_hospitals = db.query(Hospital).count()

    total_ambulances = db.query(Ambulance).count()

    total_emergencies = db.query(EmergencyRequest).count()

    available_ambulances = (
        db.query(Ambulance)
        .filter(Ambulance.status == "Available")
        .count()
    )

    available_beds = (
        db.query(Hospital.available_beds)
        .all()
    )

    total_available_beds = sum(
        bed[0] for bed in available_beds
    )

    return {
        "total_patients": total_patients,
        "total_hospitals": total_hospitals,
        "total_ambulances": total_ambulances,
        "total_emergencies": total_emergencies,
        "available_ambulances": available_ambulances,
        "available_beds": total_available_beds
    }