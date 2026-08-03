from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database.base import Base


class EmergencyRequest(Base):
    __tablename__ = "emergency_requests"

    id = Column(Integer, primary_key=True, index=True)

    patient_id = Column(Integer, ForeignKey("patients.id"))
    hospital_id = Column(Integer, ForeignKey("hospitals.id"))
    ambulance_id = Column(Integer, ForeignKey("ambulances.id"))

    emergency_type = Column(String(100), nullable=False)
    location = Column(String(200), nullable=False)
    status = Column(String(50), nullable=False)

    # Relationship with Patient
    patient = relationship(
        "Patient",
        back_populates="emergencies"
    )

    # Relationship with Hospital
    hospital = relationship(
        "Hospital",
        back_populates="emergencies"
    )

    # Relationship with Ambulance
    ambulance = relationship(
        "Ambulance",
        back_populates="emergencies"
    )