import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config_data.config import API_TOKEN
from handlers import common_handlers, student_handlers, admin_handlers
from keyboards.for_main_menu import set_main_menu

storage = MemoryStorage()


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot: Bot = Bot(token=API_TOKEN, parse_mode="HTML")
    dp: Dispatcher = Dispatcher(storage=storage)
    dp.startup.register(set_main_menu)
    logging.basicConfig(level=logging.INFO)

    dp.include_router(admin_handlers.router)
    dp.include_router(student_handlers.router)
    dp.include_router(common_handlers.router)
    # And the run events dispatching
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
