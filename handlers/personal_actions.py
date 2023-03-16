import emoji
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
item1 = types.KeyboardButton("Саши")
item2 = types.KeyboardButton("Ромы")
markup_who.add(item1, item2)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.bot.send_message(message.from_user.id, "Добро пожаловать!", reply_markup=markup)

@dp.message_handler()
async def message(message: types.Message):
    global count, lines, price_count, price_1, price_2, vremen_mas
    msg = message['text']
    if count == 0:
        if msg == "Загрузить прайс":
            await message.bot.send_message(message.from_user.id, 'Прайс какого поставщика?', reply_markup=markup_who)
        if msg == "Саши":
            price_count = 0
            await message.reply("Отправьте мне прайс одним сообщением")
            count = 1
        if msg == "Ромы":
            price_count = 1
            await message.reply("Отправьте мне прайс одним сообщением")
            count = 1
    elif count == 1:

# -------------- Загрузка прайса Саши ----------------

        if price_count == 0:
            count = 0

            price_text = msg
            lines = price_text.split('\n')
            lines = [x for x in lines if x]
            #print(lines)
            for i in range(0, len(lines)):
                vremen_mas = lines[i]
                vremen_mas = vremen_mas.split(' ')[0][0] + vremen_mas.split(' ')[0][1]

                lines[i] = lines[i].split(' ', 2)[2]

                lines[i] = lines[i].split(' -', 1)
                lines[i][1] = float(lines[i][1].replace(' ', ''))

                lines[i].insert(0, vremen_mas)
                #print(lines[i])
            price_1 = lines

# -------------- Загрузка прайса Ромы ----------------

        if price_count == 1:
            count = 0

            price_text = msg
            lines = price_text.split('\n')
            lines = [x for x in lines if x]

            #print(lines)
            for i in range(0, len(lines)):
                lines[i] = lines[i].split(' ')
                lines[i] = ' '.join(lines[i]).split()
                for j in range(0, len(lines[i])):
                    if ":" in emoji.demojize(lines[i][j]):

                        vremen_mas = []
                        emoji_flag = lines[i][j]

                        for l in range(0, j):
                            vremen_mas.append(str(lines[i][l]))

                        vremen_str = ' '.join(vremen_mas)
                        vremen_mas = []
                        vremen_mas.append(emoji_flag)
                        vremen_mas.append(vremen_str)
                        for l in range(j + 1, len(lines[i])):
                            vremen_mas.append(lines[i][l])
                        #print(vremen_mas)
            price_2 = vremen_mas
        print(price_1)
        print(price_2)
        await message.bot.send_message(message.from_user.id, 'Прайс записан', reply_markup=markup)

    if count == 0 and msg == "Сгенерить ценники":
        await message.bot.send_message(message.from_user.id, 'Отправьте запрос одним сообщением', reply_markup=markup)
        count = 2
    elif count == 2:
        price_mas=[]
        zapros = msg.split('\n')

        print(zapros)
        for i in range(0, len(price_1)):
            for j in range(0, len(zapros)):
                if zapros[j] == price_1[i][1]:
                    price_mas.append(price_1[i])
        price_mas_text = '\n'.join(' - '.join(map(str, l)) for l in price_mas)
        await message.bot.send_message(message.from_user.id, 'Саша\n'+price_mas_text, reply_markup=markup)

        price_mas = []
        for i in range(0, len(price_2)):
            for j in range(0, len(zapros)):
                print(j)
                if zapros[j] == price_2[i][1]:
                    price_mas.append(price_2[i])
                    print(price_2[i])
        price_mas_text = '\n'.join(' - '.join(map(str, l)) for l in price_mas)
        await message.bot.send_message(message.from_user.id, 'Рома\n'+price_mas_text, reply_markup=markup)
        count = 0




