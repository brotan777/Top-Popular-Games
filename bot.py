import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# Встав свій токен бота
TOKEN = "ТВОЙ_ТОКЕН_БОТА"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Посилання на твої GitHub Pages
WEB_APP_URL = "https://brotan777.github.io/Top-Popular-Games/"

@dp.message(Command("start"))
async def cmd_start(message: Message):
    # Головне меню з кнопкою Web App
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🚀 Відкрити Cyber Hub (Міні-додаток)", web_app=WebAppInfo(url=WEB_APP_URL))],
        [InlineKeyboardButton(text="💎 Курс Айбека (AJ)", callback_data="aibek_info")],
        [InlineKeyboardButton(text="ℹ️ Про проєкт", callback_data="about")]
    ])
    
    await message.answer(
        "Вітаю у сучасному геймінг-хабі та крипто-біржі **Aibek**! 🌟\n\n"
        "Обери потрібний розділ у меню нижче:",
        reply_markup=keyboard,
        parse_mode="Markdown"
    )

@dp.callback_query(F.data == "aibek_info")
async def aibek_info_callback(callback):
    await callback.message.answer(
        "💎 **Валюта Айбек (AJ)**\n\n"
        "• Базовий курс: 1$ USA = 3.77 AJ\n"
        "• Курс постійно коливається на ринку залежно від активності.\n"
        "• Відкривай міні-додаток, щоб переглядати статистику за дні та робити ставки на курс!",
        parse_mode="Markdown"
    )
    await callback.answer()

@dp.callback_query(F.data == "about")
async def about_callback(callback):
    await callback.message.answer(
        "🎮 **Top Popular Games & Aibek Hub**\n"
        "Найсучасніший міні-додаток у Telegram з кібер-дизайном, розумним ШІ та економікою.",
        parse_mode="Markdown"
    )
    await callback.answer()

async def main():
    logging.basicConfig(level=logging.INFO)
    print("Бот успішно запущено!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# Встав свій токен бота
TOKEN = "9249373827:AAFcedRT53nR2cyC09VxtvcZlKfd7Dtfrqk"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Посилання на твої GitHub Pages
WEB_APP_URL = "https://brotan777.github.io/Top-Popular-Games/"

@dp.message(Command("start"))
async def cmd_start(message: Message):
    # Головне меню з кнопкою Web App
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🚀 Відкрити Cyber Hub (Міні-додаток)", web_app=WebAppInfo(url=WEB_APP_URL))],
        [InlineKeyboardButton(text="💎 Курс Айбека (AJ)", callback_data="aibek_info")],
        [InlineKeyboardButton(text="ℹ️ Про проєкт", callback_data="about")]
    ])
    
    await message.answer(
        "Вітаю у сучасному геймінг-хабі та крипто-біржі **Aibek**! 🌟\n\n"
        "Обери потрібний розділ у меню нижче:",
        reply_markup=keyboard,
        parse_mode="Markdown"
    )

@dp.callback_query(F.data == "aibek_info")
async def aibek_info_callback(callback):
    await callback.message.answer(
        "💎 **Валюта Айбек (AJ)**\n\n"
        "• Базовий курс: 1$ USA = 3.77 AJ\n"
        "• Курс постійно коливається на ринку залежно від активності.\n"
        "• Відкривай міні-додаток, щоб переглядати статистику за дні та робити ставки на курс!",
        parse_mode="Markdown"
    )
    await callback.answer()

@dp.callback_query(F.data == "about")
async def about_callback(callback):
    await callback.message.answer(
        "🎮 **Top Popular Games & Aibek Hub**\n"
        "Найсучасніший міні-додаток у Telegram з кібер-дизайном, розумним ШІ та економікою.",
        parse_mode="Markdown"
    )
    await callback.answer()

async def main():
    logging.basicConfig(level=logging.INFO)
    print("Бот успішно запущено!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

