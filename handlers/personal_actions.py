from aiogram import types
from dispatcher import dp
import re

global markup, markup_mood
count = 0

# -.-.-.-.-.-.-.-.-.-.-.-.- Таблица меню -.-.-.-.-.-.-.-.-.-.-.-.-

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Загрузить прайс")
item2 = types.KeyboardButton("Сгенерить ценники")
item3 = types.KeyboardButton("Пустышка")
markup.add(item1, item2, item3)



@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.bot.send_message(message.from_user.ida, "Добро пожаловать!", reply_markup=markup)

@dp.message_handler()
async def message(message: types.Message):
    global count, lines
    msg = message['text']
    print(count)
    if count == 0:
        if msg == "Загрузить прайс":
            await message.reply("Отправьте мне прайс одним сообщением")
            count = 1
        print(count)
    elif count == 1:
        print(msg)
        count = 0

        price_text = msg
        lines = []
        lines = price_text.split('\n')
        c = 0
        lines = [x for x in lines if x]

        for i in range(0, len(lines)):
            lines[i] = lines[i].split(' ', 2)[2]

            lines[i] = lines[i].split(' -', 1)
            lines[i][1] = float(lines[i][1].replace(' ', ''))
            print(lines[i])

        print(lines[0][0])
        await message.bot.send_message(message.from_user.id, '1', reply_markup=markup)
    elif count == 0:
        if msg == "Сгенерить ценники":
            await message.bot.send_message(message.from_user.id, 'Отправьте запрос одним сообщением', reply_markup=markup)
            count=2
    elif count == 2:
        zapros = msg
        for i in range(0, len(lines)):
            



