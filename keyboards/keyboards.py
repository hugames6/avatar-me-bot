from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_next = KeyboardButton('А что ты умеешь?')
help = KeyboardButton('Помощь')

first_step = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

first_step.row(start_next, help)