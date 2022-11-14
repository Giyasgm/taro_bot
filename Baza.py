from aiogram import Bot, Dispatcher

from aiogram.contrib.fsm_storage.memory import MemoryStorage

from aiogram.dispatcher.filters.state import StatesGroup, State


TOKEN = "5630934030:AAFTv2Z7nUfXprKDZuPlcJmRlVE9e8Hh2G0"

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class Testik(StatesGroup):
    test1 = State()
