import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from config import BOT_TOKEN
from keyboard import web_app
logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Для работы с ботом нужно использовать web-app",reply_markup=web_app)

@dp.message()
async def echo(message: types.Message):
    await message.answer("Для работы с ботом нужно использовать web-app",reply_markup=web_app)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())