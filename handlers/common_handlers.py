from aiogram import Router
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import Message

from keyboards.for_start import main_keyboard
from lexicon import rus

router = Router()


@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer("Выберите команду", reply_markup=main_keyboard)


@router.message(Command(commands=["help"]))
async def process_help_command(message: Message):
    await message.answer(rus.help_message)


@router.message(Command(commands=["checkin"]))
@router.message(Text(text="Отметить своё посещение"))
async def checkin_not_registered(message: Message):
    first_name = message.from_user.first_name
    await message.answer(
        f"{first_name}, Вы не зарегистрированы в базе. Обратитесь к администратору."
    )


@router.message(Command(commands=["add_student"]))
@router.message(Text(text="Добавить студентов в базу"))
async def not_admin(message: Message):
    await message.answer(
        "Вы не обладаете привилегиями администратора, чтобы запустить эту команду."
    )


@router.message(Command(commands=["report"]))
@router.message(Text(text="Отчёт о посещаемости"))
async def not_admin(message: Message):
    await message.answer(
        "Вы не обладаете привилегиями администратора, чтобы запустить эту команду."
    )


@router.message()
async def any_text(message: Message):
    await message.answer(rus.unknown_text)
