from aiogram.fsm.state import State, StatesGroup


class AttendanceStates(StatesGroup):
    waiting_for_location = State()
    checked_in = State()
