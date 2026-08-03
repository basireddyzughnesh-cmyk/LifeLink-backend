from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database.base import Base


class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    age = Column(Integer)
    gender = Column(String(20))
    blood_group = Column(String(10))
    phone = Column(String(15))
    address = Column(String(200))

    # Relationship with EmergencyRequest
    emergencies = relationship(
        "EmergencyRequest",
        back_populates="patient"
    )