from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from keyboards import first_step
from bot import bot

async def start(message:Message):
    await bot.send_message(message.from_user.id, 'Добро пожаловать в бот-генератора аватарок!', reply_markup=first_step)

def reg_hendlers_user(dp:Dispatcher):
    dp.register_message_handler(start, commands=['start'])