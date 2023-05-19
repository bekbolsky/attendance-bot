from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


location_button = KeyboardButton(text="Отправить геолокацию", request_location=True)
location_kb = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[[location_button]],
    one_time_keyboard=True,
)
