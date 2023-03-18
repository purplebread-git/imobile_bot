import emoji, openpyxl
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
markup_who.add(item1, item2)

markup_zapros_to_excel = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Записать результаты в Excel")
item2 = types.KeyboardButton("Назад")
markup_zapros_to_excel.add(item1, item2)

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




@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.bot.send_message(message.from_user.id, "Добро пожаловать!", reply_markup=markup)


@dp.message_handler()
async def message(message: types.Message):
    global count, lines, price_count, price_1, price_2, vremen_mas, price_mas, price_mas1
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
            print(price_2)
        await message.bot.send_message(message.from_user.id, 'Прайс записан', reply_markup=markup)

# ---------------------------- Генерация прайса по запросу -----------------------------

    elif count == 0 and msg == "Сгенерить ценники":
        await message.bot.send_message(message.from_user.id, 'Отправьте запрос одним сообщением', reply_markup=types.ReplyKeyboardRemove())
        count = 2
    elif count == 2:
        price_mas = []
        zapros = msg.split('\n')
        price_mas1 = []
        count = 0
        print(zapros)

        for i in range(0, len(price_1)):
            for j in range(0, len(zapros)):
                if zapros[j].lower() == price_1[i][1].lower():
                    price_mas.append(price_1[i])
        print(price_mas)
        price_mas_text = '\n'.join(' - '.join(map(str, l)) for l in price_mas)
        await message.bot.send_message(message.from_user.id, 'Саша\n' + price_mas_text, reply_markup=markup)

        for i in range(0, len(price_2)):
            for j in range(0, len(zapros)):
                if zapros[j].lower() == price_2[i][1].lower():
                    price_mas1.append(price_2[i])
        print(price_mas1)
        price_mas_text = '\n'.join(' - '.join(map(str, l)) for l in price_mas1)
        await message.bot.send_message(message.from_user.id, 'Рома\n' + price_mas_text, reply_markup=markup_zapros_to_excel)

    elif msg == "Записать весь прайс в Excel":
        if count == 0:
            price_to_excel(price_1, price_2)
            await message.bot.send_message(message.from_user.id, 'Прайс записан в Excel', reply_markup=markup)
            print('Прайс Записан в Excel')
    elif msg == "Записать результаты в Excel":
        price_to_excel(price_mas, price_mas1, "result_price")
    elif msg == 'Назад':
        count = 0
        await message.bot.send_message(message.from_user.id, 'Возвращаюсь', reply_markup=markup)
    else:
        print("Ошибка")
        await message.bot.send_message(message.from_user.id, 'Ошибка', reply_markup=markup)
        count = 0
