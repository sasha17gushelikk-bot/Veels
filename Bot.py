import asyncio
from aiogram import Bot, Dispatcher, F, types
from aiogram.enums import ParseMode

TOKEN = "8965091596:AAE1AYDvQVCApuoYM2yJnw1nAbGgqmHKPqY"

bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

@dp.message(F.text == "/start")
async def start(msg: types.Message):
    await msg.answer("🤖 Бот работает успешно!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
