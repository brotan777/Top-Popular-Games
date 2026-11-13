import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

TOKEN = "9249373827:AAFcedRT53nR2cyC09VxtvcZlKfd7Dtfrqk"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Створюємо кнопку для міні-додатка
game_button = InlineKeyboardButton(
    text="🎮 Відкрити ігровий міні-додаток", 
    web_app=WebAppInfo(url="https://brotan777.github.io")
)
keyboard = InlineKeyboardMarkup(inline_keyboard=[[game_button]])

# Обробник команди /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "Привіт! Вітаю в нашому ігровому клубі! 🎮\n"
        "Скоро тут з'являться Мафія, Уно, Карти та інші круті ігри. Тисни кнопку нижче!",
        reply_markup=keyboard
    )

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
