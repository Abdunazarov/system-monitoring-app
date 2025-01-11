from sqlalchemy import Column, Integer, Float, DateTime
from datetime import datetime
from db_setup import Base

class SystemUsage(Base):
    __tablename__ = "system_usage"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.now())
    cpu_usage = Column(Float, nullable=False)
    ram_total = Column(Float, nullable=False)
    ram_free = Column(Float, nullable=False)
    disk_total = Column(Float, nullable=False)
    disk_free = Column(Float, nullable=False)
