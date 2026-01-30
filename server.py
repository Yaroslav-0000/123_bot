import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TOKEN = "8239139777:AAEl9icv7_AXk4cxX0KBpOMqUEhXHNnG7uI"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("123")

@dp.message(Command("help"))
async def help_handler(message: types.Message):
    await message.answer("=/start=")

@dp.message()
async def echo_handler(message: types.Message):
    if "123" in message.text.lower():
        await message.answer("---___123___---")
    elif "test" in message.text.lower():
        await message.answer("^Hello^")
    else:
        await message.answer(f": {message.text}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
