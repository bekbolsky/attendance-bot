from aiogram.fsm.state import State, StatesGroup


class RegistrationStates(StatesGroup):
    adding_students = State()

