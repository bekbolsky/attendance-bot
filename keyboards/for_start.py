from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


command_buttons = [
    [
        KeyboardButton(
            text="Отметить своё посещение",
        )
    ],
    [KeyboardButton(text="Добавить студентов в базу")],
    [KeyboardButton(text="Отчёт о посещаемости")],
]
main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=command_buttons)
