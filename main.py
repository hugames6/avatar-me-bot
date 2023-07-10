from aiogram import executor
from bot import dp
from hendlers import user

async def on_start(_):
    print('Бот запущен')
    # await sql_start()

async def on_shut(_):
    pass

user.reg_hendlers_user(dp)
executor.start_polling(dp, skip_updates=True, on_startup=on_start)