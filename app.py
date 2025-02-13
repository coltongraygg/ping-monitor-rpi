from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orgm import mapped_column
from fastapi import FastAPI
from sqlalchemy import Date
# define database url with database (sqlite), driver (pysqlite), and then path to save db file
DATABASE_URL = 'sqlite+pysqlite:///home/colton/projects/ping_monitor/network_data.db'




class Base(DeclaritiveBase):
  pass

class Database(Base):
  __tablename__ = 'ping_tests'
  id: Mapped[int] = mapped_column(primary_key=True)
  ping_address: Mapped[str] 
  hop: Mapped[int]
  hop_ip_address: Mapped[str]
  hop_hostname: Mapped[str]
  packet_loss: Mapped[float]
  location: Mapped[str]
  date_time: Mapped[Date]



# establish connection to db via sqlalchemy create_engine
engine = create_engine(DATABASE_URL, echo=True)
Base.metadata.create_all(engine)