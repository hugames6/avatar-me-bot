from aiogram import executor
from bot import dp, storage
from hendlers import user
from database import sql_start

async def on_start(_):
    print('Бот запущен')
    await sql_start()

async def on_shut(_):
    await storage.close()

user.reg_hendlers_user(dp)
executor.start_polling(dp, skip_updates=True, on_startup=on_start, on_shutdown=on_shut)