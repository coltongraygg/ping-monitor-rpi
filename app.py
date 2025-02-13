from sqlalchemy import create_engine, DateTime, Integer, String, Float, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from fastapi import FastAPI
from datetime import datetime

# define database url with database (sqlite), driver (pysqlite), and then path to save db file
DATABASE_URL = 'sqlite+pysqlite:///home/colton/projects/ping_monitor/pings.db'




class Base(DeclarativeBase):
  pass

class Pings(Base):
  __tablename__ = 'ping_tests'
  id: Mapped[int] = mapped_column(primary_key=True)
  ping_address: Mapped[str]  = mapped_column(String)
  hop: Mapped[int] = mapped_column(Integer)
  hop_ip_address: Mapped[str] = mapped_column(String)
  hop_hostname: Mapped[str] = mapped_column(String)
  packet_loss: Mapped[float] = mapped_column(Float)
  location: Mapped[str] = mapped_column(String)
  time_created: Mapped[datetime] = mapped_column(DateTime, default=func.now())



# establish connection to db via sqlalchemy create_engine
engine = create_engine(DATABASE_URL, echo=True)
Base.metadata.create_all(engine) # execute