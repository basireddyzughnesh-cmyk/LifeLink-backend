from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from database.base import Base


class Hospital(Base):
    __tablename__ = "hospitals"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)
    location = Column(String(200), nullable=False)
    phone = Column(String(15), nullable=False)

    total_beds = Column(Integer, nullable=False)
    available_beds = Column(Integer, nullable=False)

    emergency_available = Column(
        Boolean,
        nullable=False,
        default=False
    )

    # Relationship with EmergencyRequest
    emergencies = relationship(
        "EmergencyRequest",
        back_populates="hospital"
    )