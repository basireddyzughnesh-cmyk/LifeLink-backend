from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database.base import Base


class Ambulance(Base):
    __tablename__ = "ambulances"

    id = Column(Integer, primary_key=True, index=True)

    vehicle_number = Column(String(20), unique=True, nullable=False)
    driver_name = Column(String(100), nullable=False)
    driver_phone = Column(String(15), nullable=False)
    current_location = Column(String(200), nullable=False)
    status = Column(String(20), nullable=False)

    # Relationship with EmergencyRequest
    emergencies = relationship(
        "EmergencyRequest",
        back_populates="ambulance"
    )