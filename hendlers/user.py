from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery

from database import sql_add_user, sql_update_tries
from keyboards import first_keyboard, second_keyboard, gender, agr
from bot import bot, dp
from config import BOT_TOKEN

import requests

import time

class FSMGetPhoto(StatesGroup):
    get_user_photo = State()
    bot_refresh_photo = State()

async def get_date():
    loc_time = time.localtime(time.time())
    date = time.strftime('%d.%m.%Y %H:%M:%S', loc_time)
    return date

async def get_id():
    id = int(time.time()) + 10800
    return id

async def start(message:Message):
    await bot.send_message(message.from_user.id, 'Добро пожаловать в бот-генератора аватарок!', reply_markup=first_keyboard)
    a = await sql_add_user(user_id=message.from_user.id, username=message.from_user.username, name=message.from_user.first_name, surname=message.from_user.last_name, date=await get_date())
    # if a != True:
    #     await user_registration(user_id=message.from_user.id)

@dp.callback_query_handler(text='ft_sp')
async def start_next(callback:CallbackQuery):
    if callback.data == 'ft_sp':
        await callback.message.answer('Я генерирую аватарки с вашим лицом на любой вкус и цвет!', reply_markup=second_keyboard)
    await callback.answer()

@dp.callback_query_handler(text='sd_sp')
async def start_fird(callback:CallbackQuery):
    if callback.data:
        await callback.message.answer('Заинтересовал? Тогда выбери свой пол!', reply_markup=gender)
    await callback.answer()

@dp.callback_query_handler(Text(startswith='gender_'))
async def user_gender_choise(callback:CallbackQuery):
    user_choise = callback.data.split('_')[1]
    if user_choise == 'male':
        await bot.send_message(callback.from_user.id, 'Вы мужчина! Приступим?', reply_markup=agr)
    elif user_choise == 'female':
        await bot.send_message(callback.from_user.id, 'Вы женщина! Приступим?', reply_markup=agr)

@dp.callback_query_handler(text='agreed')
async def get_photo(message:Message):
    await bot.send_message(message.from_user.id, 'Просто загрузите мне своё фото! Но только лишь одно!')

async def refreshing_photo(message:Message):
    await bot.send_message(message.from_user.id, 'Вы отправили фото!')
    file_id = message.photo[-1].file_id
    uri = f"https://api.telegram.org/bot/{BOT_TOKEN}/getFile?file_id={file_id}"
    response = requests.get(uri)
    print(uri)
    print(response.json())
    b =  await sql_update_tries(user_id=message.from_user.id)
    if b == True:
        await bot.send_photo(message.from_user.id, photo=file_id)
    elif b == False:
        await bot.send_message(message.from_user.id, 'У вас закончились попытки!')


def reg_hendlers_user(dp:Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(refreshing_photo, content_types=['photo'])
