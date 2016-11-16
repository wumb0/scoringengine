from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship

from scoring_engine.models.base import Base


class Round(Base):
    __tablename__ = "rounds"
    id = Column(Integer, primary_key=True)
    number = Column(Integer, nullable=False)
    checks = relationship("Check", back_populates="round")