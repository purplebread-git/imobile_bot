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

markup_who = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Рома")
item2 = types.KeyboardButton("???")
markup.add(item1, item2)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.bot.send_message(message.from_user.id, "Добро пожаловать!", reply_markup=markup)

@dp.message_handler()
async def message(message: types.Message):
    global count, lines
    msg = message['text']
    if count == 0:
        if msg == "Загрузить прайс":
            await message.bot.send_message(message.from_user.id, 'Прайс какого поставщика?', reply_markup=markup_who)
            if msg == "Рома":
                price_count = 0
                await message.reply("Отправьте мне прайс одним сообщением")
                count = 1
            if msg == "???":
                price_count = 1
                await message.reply("Отправьте мне прайс одним сообщением")
                count = 1
    elif count == 1:
        print(msg)
        count = 0

        price_text = msg
        lines = price_text.split('\n')
        c = 0
        lines = [x for x in lines if x]
        print(lines)
        for i in range(0, len(lines)):
            lines[i] = lines[i].split(' ', 2)[2]

            lines[i] = lines[i].split(' -', 1)
            lines[i][1] = float(lines[i][1].replace(' ', ''))
            print(lines[i])


        await message.bot.send_message(message.from_user.id, '1', reply_markup=markup)

    if count == 0 and msg == "Сгенерить ценники":
        await message.bot.send_message(message.from_user.id, 'Отправьте запрос одним сообщением', reply_markup=markup)
        count = 2
    elif count == 2:
        price_mas=[]
        zapros = msg.split('\n')
        print(zapros)
        for i in range(0, len(lines)):
            for j in range(0, len(zapros)):
                if zapros[j] == lines[i][0]:
                    price_mas.append(lines[i])
                    print(lines[i])
        price_mas_text = '\n'.join(' - '.join(map(str, l)) for l in price_mas)
        await message.bot.send_message(message.from_user.id, price_mas_text, reply_markup=markup)


        count = 0




