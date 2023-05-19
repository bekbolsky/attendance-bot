from aiogram import Router
from aiogram.filters import Command, Text
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from config_data.config import ADMIN_IDS
from filters.admin import IsAdmin
from states.registration import RegistrationStates
from utils import methods
from lexicon import rus

router = Router()
router.message.filter(IsAdmin(ADMIN_IDS))


@router.message(Command(commands=["add_students"]))
@router.message(Text(text="Добавить студентов в базу"))
async def add_students(message: Message, state: FSMContext):
    await message.answer(rus.enter_student_list)
    await state.set_state(RegistrationStates.adding_students)


@router.message(RegistrationStates.adding_students)
async def process_add_students(message: Message, state: FSMContext):
    students = message.text
    students = students.split("\n")
    print(students)
    try:
        methods.add_students_to_db(students)
        await message.answer("Студенты успешно добавлены в базу данных")
        await state.clear()
    except ValueError:
        await message.answer("Не хватает значении в списке студентов.")
    except Exception as exc:
        await message.answer(f"Произошла ошибка при добавлении в базу данных. {exc}")


@router.message(Command(commands=["report"]))
@router.message(Text(text="Отчёт о посещаемости"))
async def process_report(message: Message):
    students = methods.get_all_students()
    # TODO: send excel file to admin
    print(students)
    await message.answer("report")
