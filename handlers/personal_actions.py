from aiogram import types
from dispatcher import dp
import re

global markup, markup_mood
count = 0

# -.-.-.-.-.-.-.-.-.-.-.-.- Таблица меню -.-.-.-.-.-.-.-.-.-.-.-.-

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("➕ Добавить запись")
item2 = types.KeyboardButton("📊  Статистика")
item3 = types.KeyboardButton("⚙️Настройки")
markup.add(item1, item2, item3)

# -.-.-.-.-.-.-.-.-.-.-.-.- Таблица выбора настроения -.-.-.-.-.-.-.-.-.-.-.-.-



@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.bot.send_message(message.from_user.id, "Добро пожаловать!", reply_markup=markup)