from datetime import datetime

import pytz
from aiogram import F, Router
from aiogram.filters import Command, Text
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from config_data.config import DISTANCE_THRESHOLD, TIMEZONE
from database.models import Student
from filters.student import IsStudentRegistered
from keyboards.for_location import location_kb
from states.attendance import AttendanceStates
from utils.distance import calculate_distance
from utils.methods import (
    add_attendance_to_db,
    get_student_by_telegram_id,
    student_is_present,
)

router = Router()
router.message.filter(IsStudentRegistered())


@router.message(Command(commands=["checkin"]))
@router.message(Text(text="Отметить своё посещение"))
async def attendance_command(message: Message, state: FSMContext):
    # Запросите геолокацию студента
    await message.answer(
        "Пожалуйста, отправьте свою геолокацию", reply_markup=location_kb
    )
    await state.set_state(AttendanceStates.waiting_for_location)


@router.message(F.content_type == "location", AttendanceStates.waiting_for_location)
async def attendance_check(message: Message, state: FSMContext):
    # Получите геолокацию студента и проверьте посещаемость
    telegram_id = message.from_user.id
    lat = message.location.latitude
    lon = message.location.longitude
    today = datetime.now(pytz.timezone(TIMEZONE))
    student: Student = get_student_by_telegram_id(telegram_id)
    distance = calculate_distance(lat, lon)
    if distance < DISTANCE_THRESHOLD:
        if not bool(student_is_present(student.id, today.date())):
            add_attendance_to_db(student.id)
            await message.answer(
                f"{student.first_name}, Вы отмечены как присутствующий. Дистанция - {distance:.0f} м.",
                reply_markup=ReplyKeyboardRemove(),
            )
            await state.set_state(AttendanceStates.checked_in)
        else:
            await message.answer(
                f"{student.first_name}, Вы уже отметились сегодня.",
                reply_markup=ReplyKeyboardRemove(),
            )
            await state.set_state(AttendanceStates.checked_in)

    else:
        await message.answer(
            f"Вы находитесь слишком далеко от колледжа. Дистанция - {distance:.0f} метр",
            reply_markup=ReplyKeyboardRemove(),
        )
        await state.clear()


@router.message(AttendanceStates.checked_in)
async def checked_in(message: Message):
    await message.answer("", reply_markup=location_kb)