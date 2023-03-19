import sys

import emoji, openpyxl, traceback
from aiogram import types
from dispatcher import dp
import re

global markup, markup_mood
count = 0

# -.-.-.-.-.-.-.-.-.-.-.-.- Таблица меню -.-.-.-.-.-.-.-.-.-.-.-.-

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Загрузить прайс")
item2 = types.KeyboardButton("Сгенерить ценники")
item3 = types.KeyboardButton("Записать весь прайс в Excel")
markup.add(item1, item2, item3)

markup_who = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Саши")
item2 = types.KeyboardButton("Ромы")
item3 = types.KeyboardButton('Назад')
markup_who.add(item1, item2, item3)

markup_zapros_to_excel = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton('Отбор лучшей цены')
item2 = types.KeyboardButton("Записать результаты в Excel")
item3 = types.KeyboardButton("Назад")
markup_zapros_to_excel.add(item1, item2, item3)

markup_percent = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton('Добавить процент')
item2 = types.KeyboardButton('Назад')
markup_percent.add(item1,item2)

def price_to_excel(price_1, price_2, name='price_full'):
    workbook = openpyxl.Workbook()
    worksheet = workbook.active
    worksheet.cell(row=1, column=1, value='Саша')
    worksheet.cell(row=1, column=4, value='Рома')
    for i in range(len(price_1)):
        for j in range(0, len(price_1[i])):
            worksheet.cell(row=i + 2, column=j + 1, value=price_1[i][j])
    for i in range(len(price_2)):
        for j in range(0, len(price_2[i])):
            worksheet.cell(row=i + 2, column=j + 4, value=price_2[i][j])
    workbook.save(filename=f'{name}.xlsx')

def filter_price(a, b):
    a_processed = []
    b_processed = []

    for el_a in a:
        for el_b in b:
            if el_a[1] == el_b[1]:
                if el_a[2] < el_b[2]:
                    a_processed.append(el_a)
                elif el_b[2] < el_a[2]:
                    b_processed.append(el_b)
                break
        else:
            a_processed.append(el_a)

    for el_b in b:
        for el_a in a:
            if el_b[1] == el_a[1]:
                break
        else:
            b_processed.append(el_b)
    return a_processed, b_processed


@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.bot.send_message(message.from_user.id, "Добро пожаловать!", reply_markup=markup)


@dp.message_handler()
async def message(message: types.Message):
    global count, lines, price_count, price_1, price_2, vremen_mas, price_mas, price_mas1, filter_price_sasha, filter_price_roma, percent
    msg = message['text']
    if msg == "Загрузить прайс":
        if count == 0:
            await message.bot.send_message(message.from_user.id, 'Прайс какого поставщика?', reply_markup=markup_who)
    elif msg == "Саши":
        if count == 0:
            price_count = 0
            await message.reply("Отправьте мне прайс одним сообщением", reply_markup=types.ReplyKeyboardRemove())
            count = 1
    elif msg == "Ромы":
        if count == 0:
            price_count = 1
            await message.reply("Отправьте мне прайс одним сообщением", reply_markup=types.ReplyKeyboardRemove())
            count = 1
    elif count == 1:

        # -------------- Загрузка прайса Саши ----------------

        if price_count == 0:
            count = 0

            price_text = msg
            lines = price_text.split('\n')
            lines = [x for x in lines if x]
            for i in range(0, len(lines)):
                vremen_mas = lines[i]
                vremen_mas = vremen_mas.split(' ')[0][0] + vremen_mas.split(' ')[0][1]

                lines[i] = lines[i].split(' ', 2)[2]

                lines[i] = lines[i].split(' -', 1)
                lines[i][1] = float(lines[i][1].replace(' ', ''))
                lines[i][1] = int(lines[i][1]*1000)
                lines[i].insert(0, vremen_mas)
            price_1 = lines
            for i in range(0, len(price_1)):
                if price_1[i][0] == "🇺🇸" and int(price_1[i][1].split(' ')[0]) ==14:
                    price_1[i] = []
            price_1 = [x for x in price_1 if x]

            print(price_1)

        # -------------- Загрузка прайса Ромы ----------------

        if price_count == 1:
            count = 0
            vremen_mas = []
            price_text = msg
            lines = price_text.split('\n')
            lines = [x for x in lines if x]
            price_2 = []
            # print(lines)
            for i in range(0, len(lines)):
                lines[i] = lines[i].split(' ')
                lines[i] = ' '.join(lines[i]).split()
                for j in range(0, len(lines[i])):
                    vremen_mas = []
                    if ":" in emoji.demojize(lines[i][j]):
                        emoji_flag = lines[i][j]

                        for l in range(0, j):
                            vremen_mas.append(str(lines[i][l]))

                        vremen_str = ' '.join(vremen_mas)
                        vremen_mas = []
                        vremen_mas.append(emoji_flag)
                        vremen_mas.append(vremen_str)
                        for l in range(j + 1, len(lines[i])):
                            vremen_mas.append(int(lines[i][l]))
                        price_2.append(vremen_mas)

            for i in range(0, len(price_2)):
                if price_2[i][0] == "🇺🇸" and int(price_2[i][1].split(' ')[0]) ==14:
                    price_2[i] = []
            price_2 = [x for x in price_2 if x]
            print(price_2)
        await message.bot.send_message(message.from_user.id, 'Прайс записан', reply_markup=markup)
        await message.bot.send_message(message.from_user.id, '(Американские модели 14-й линейки в прайс не записываются)', reply_markup=markup)

# ---------------------------- Генерация прайса по запросу -----------------------------

    elif count == 0 and msg == "Сгенерить ценники":
        try:
            print(price_1)
            print(price_2)
            count = 2
            await message.bot.send_message(message.from_user.id, '<b>Отправьте запрос одним сообщением</b>\n<i>В формате:\n"Название модели" "Объем памяти" "Цвет"</i>', reply_markup=types.ReplyKeyboardRemove())
        except:
                await message.bot.send_message(message.from_user.id, 'Загрузите 2 прайса для генерации',reply_markup=markup)
                tb = sys.exc_info()[2]
                print(traceback.format_tb(tb)[0])

    elif count == 2:
        price_mas = []
        count = 0
        zapros = msg.split('\n')
        price_mas1 = []
        print(zapros)

        for i in range(0, len(price_1)):
            for j in range(0, len(zapros)):
                if zapros[j].lower() == price_1[i][1].lower():
                    price_mas.append(price_1[i])
        print(price_mas)
        price_mas_text = '\n'.join(' - '.join(map(str, l)) for l in price_mas)
        await message.bot.send_message(message.from_user.id, '<b>Саша</b>\n' + price_mas_text, reply_markup=markup)

        for i in range(0, len(price_2)):
            for j in range(0, len(zapros)):
                if zapros[j].lower() == price_2[i][1].lower():
                    price_mas1.append(price_2[i])
        print(price_mas1)
        price_mas_text = '\n'.join(' - '.join(map(str, l)) for l in price_mas1)
        await message.bot.send_message(message.from_user.id, '<b>Рома</b>\n' + price_mas_text, reply_markup=markup_zapros_to_excel)
    elif msg == 'Отбор лучшей цены':
        print('price_mas - ', price_mas)
        print('price_mas1 - ', price_mas1)

        fil = filter_price(price_mas, price_mas1)
        filter_price_sasha = fil[0]
        print(filter_price_sasha)
        filter_price_roma = fil[1]
        print(filter_price_roma)
        price_mas_text = '\n'.join(' - '.join(map(str, l)) for l in filter_price_sasha)
        await message.bot.send_message(message.from_user.id, '<b>Саша</b>', reply_markup=markup_percent)
        await message.bot.send_message(message.from_user.id, price_mas_text, reply_markup=markup_percent)
        price_mas_text = '\n'.join(' - '.join(map(str, l)) for l in filter_price_roma)
        await message.bot.send_message(message.from_user.id, '<b>Рома</b>', reply_markup=markup_percent)
        await message.bot.send_message(message.from_user.id, price_mas_text, reply_markup=markup_percent)

        count = 0
    elif msg == 'Добавить процент':
        count = 'percent'
        await message.bot.send_message(message.from_user.id, 'Какой процент необходим добавить?\nНапишите просто цифрой', reply_markup=types.ReplyKeyboardRemove())
    elif count == 'percent':
        percent = int(msg)
        for i in range(0, len(filter_price_sasha)):
            filter_price_sasha[i][2] = int(round(((filter_price_sasha[i][2] + int(filter_price_sasha[i][2] * percent / 100)) / 100), 0) * 100)
        for i in range(0, len(filter_price_roma)):
            filter_price_roma[i][2] = int(round(((filter_price_roma[i][2] + int(filter_price_roma[i][2] * percent / 100)) / 100), 0) * 100)
        price_mas_text = '\n'.join(' - '.join(map(str, l)) for l in filter_price_sasha)
        await message.bot.send_message(message.from_user.id, '<b>Саша</b>', reply_markup=markup_percent)
        await message.bot.send_message(message.from_user.id, price_mas_text, reply_markup=markup_percent)
        price_mas_text = '\n'.join(' - '.join(map(str, l)) for l in filter_price_roma)
        await message.bot.send_message(message.from_user.id, '<b>Рома</b>', reply_markup=markup_percent)
        await message.bot.send_message(message.from_user.id, price_mas_text, reply_markup=markup)


    elif msg == "Записать весь прайс в Excel":
        try:
            print(price_1)
            print(price_2)
            price_to_excel(price_1, price_2)
            await message.bot.send_message(message.from_user.id, 'Прайс записан в Excel', reply_markup=markup)
            await message.bot.send_document(message.from_user.id, (open('price_full.xlsx', 'rb')))
            count = 0
        except:
            await message.bot.send_message(message.from_user.id, 'Загрузите 2 прайса для записи', reply_markup=markup)

    elif msg == "Записать результаты в Excel":
        price_to_excel(price_mas, price_mas1, "result_price")
        await message.bot.send_document(message.from_user.id, (open('result_price.xlsx', 'rb')))
    elif msg == 'Назад':
        count = 0
        await message.bot.send_message(message.from_user.id, 'Возвращаюсь', reply_markup=markup)
    else:
        print("Ошибка")
        await message.bot.send_message(message.from_user.id, 'Ошибка', reply_markup=markup)
        count = 0
