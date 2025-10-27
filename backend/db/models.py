from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from datetime import datetime
from .database import Base

class Analysis(Base):
    __tablename__ = "analysis_results"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False)
    label = Column(String, nullable=False)
    score = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
