from typing import List

from sqlalchemy.exc import IntegrityError
from sqlalchemy import select, insert, func

from database.connection import Session
from database.models import Attendance, Student


def add_students_to_db(student_data: List[str]):
    """Добавляет студента в базу данных"""
    with Session() as session:
        Students = []
        for line in student_data:
            last_name, first_name, middle_name, group_name, telegram_id = line.split(
                ","
            )
            student = Student(
                last_name=last_name.strip(),
                first_name=first_name.strip(),
                middle_name=middle_name.strip(),
                group_name=group_name.strip(),
                telegram_id=telegram_id.strip(),
            )
            Students.append(student)

        session.add_all(Students)
        try:
            session.commit()
        except IntegrityError:
            session.rollback()


def get_all_students():
    """Возвращает список всех студентов"""
    with Session() as session:
        stmt = select(Student).order_by(Student.id)
        all_students = session.execute(stmt).scalars()
    return all_students


def get_student_by_telegram_id(telegram_id):
    """Возвращает студента по его telegram_id"""
    with Session() as session:
        stmt = select(Student).where(Student.telegram_id == telegram_id)
        student = session.execute(stmt).scalar()
    return student


def add_attendance_to_db(id):
    """Добавляет запись о посещении студента в базу данных"""
    with Session() as session:
        stmt = insert(Attendance).values(student_id=id, is_present=True)
        session.execute(stmt)
        session.commit()


def get_attendance_by_date(date):
    """Возвращает список посещений за определенную дату"""
    with Session() as session:
        stmt = (
            select(
                Student.first_name, func.DATE(Attendance.date), Attendance.is_present
            )
            .join(Attendance)
            .where(func.DATE(Attendance.date) == date)
        )
        attendances = session.execute(stmt).scalars()

    return attendances


def student_is_present(student_id, date):
    with Session() as session:
        stmt = (
            select(Attendance.is_present)
            .where(Attendance.student_id == student_id)
            .where(func.DATE(Attendance.date) == date)
        )
        is_present = session.execute(stmt).scalar()
    return is_present


def get_dates_in_attendance():
    with Session() as session:
        stmt = select(func.DATE(Attendance.date))
        result = session.execute(stmt).scalars()
    return result
