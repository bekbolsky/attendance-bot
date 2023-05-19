from datetime import datetime

from pytz import timezone
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, relationship
from config_data.config import TIMEZONE


class Base(DeclarativeBase):
    pass


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    first_name = Column(String(50), index=True, nullable=False)
    last_name = Column(String(50), index=True, nullable=False)
    middle_name = Column(String(50), index=True, nullable=True)
    group_name = Column(String(30), index=True, nullable=False)
    telegram_id = Column(Integer, unique=True, index=True, nullable=False)
    attendance = relationship("Attendance", back_populates="student")


class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    date = Column(DateTime(timezone=True), default=datetime.now(timezone(TIMEZONE)))
    is_present = Column(Boolean, default=False)
    student_id = Column(Integer, ForeignKey("students.id"))
    student = relationship("Student", back_populates="attendance")
