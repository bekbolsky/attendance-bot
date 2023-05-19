from aiogram import Bot
from aiogram.types import BotCommand


async def set_main_menu(bot: Bot):
    """Создаем список с командами и их описанием для кнопки menu"""
    main_menu_commands = [
        BotCommand(command="/help", description="Справка по работе бота"),
        BotCommand(command="/checkin", description="Отметить своё посещение"),
        BotCommand(
            command="/add_students", description="Добавить в БД список студентов"
        ),
        BotCommand(command="/report", description="Отчёт о посещаемости"),
    ]

    await bot.set_my_commands(main_menu_commands)
