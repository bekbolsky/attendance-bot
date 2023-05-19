from aiogram.filters import BaseFilter
from aiogram.types import Message

from utils.methods import get_student_by_telegram_id


class IsStudentRegistered(BaseFilter):
    """Кастомный фильтр для проверки регистрации студента в базе."""

    async def __call__(self, message: Message) -> bool:
        telegram_id = message.from_user.id
        student = get_student_by_telegram_id(telegram_id)
        return bool(student)
