import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor

API_TOKEN = '6808466446:AAEJ0sEzC49Rka7VVqhm65biXPz5X7bzfEk'
ADMIN_ID = 7071251777  # замените на ID администратора

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

async def send_status():
    await bot.send_message(ADMIN_ID, "Бот работает")
    await asyncio.sleep(1)  # Ждем 1 секунду перед следующей отправкой
    asyncio.create_task(send_status())  # Планируем следующую отправку

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Бот запущен и работает.")
    asyncio.create_task(send_status())  # Запуск функции отправки сообщений после команды /start

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
