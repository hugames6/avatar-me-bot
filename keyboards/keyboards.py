from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

first_step = InlineKeyboardButton(text='А что ты умеешь?', callback_data='ft_sp')
help = InlineKeyboardButton(text='Помощь', callback_data='hp')
second_step = InlineKeyboardButton(text='Дальше...', callback_data='sd_sp')
m = InlineKeyboardButton(text='Мужчина', callback_data='gender_male')
f = InlineKeyboardButton(text='Женщина', callback_data='gender_female')
agreed = InlineKeyboardButton(text='Приступим!', callback_data='agreed')

first_keyboard = InlineKeyboardMarkup()
second_keyboard = InlineKeyboardMarkup()
gender = InlineKeyboardMarkup()
agr = InlineKeyboardMarkup()

first_keyboard.row(first_step, help)
second_keyboard.row(second_step, help)
gender.row(m, f)
agr.row(agreed)