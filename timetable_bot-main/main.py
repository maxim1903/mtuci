import datetime
import psycopg2
import telebot
from telebot import types

token = "2113287709:AAEQLuoZQRTeaK3Bqk46A-mNl9xGw_qDo1w"
bot = telebot.TeleBot(token)
date = datetime.date.today().isocalendar()[1]

conn = psycopg2.connect(database="postgres",
                        user="postgres",
                        password="3308_Blbgh",
                        host="localhost",
                        port="5432")

cursor = conn.cursor()


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Расписание на текущую неделю",
                 "Расписание на следующую неделю")
    bot.send_message(message.chat.id, 'Здесь можно посмотреть расписание БФИ2102', reply_markup=keyboard)


@bot.message_handler(commands=['week'])
def week(message):
    if date % 2 == 0:
        bot.send_message(message.chat.id, 'Сейчас нижняя неделя')
    if date % 2 == 1:
        bot.send_message(message.chat.id, 'Сейчас верхняя неделя')


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, '''Данный бот присылает расписание.

                                        /week - Текущая неделя
                                        /help - Помощь
                                        /mtuci - Ссылка на официальный сайт МТУСИ''')

@bot.message_handler(commands=['mtuci'])
def mtuci(message):
    bot.send_message(message.chat.id, 'https://mtuci.ru/')

@bot.message_handler(content_types=['text'])
def dododo(message):
    days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница']
    week = datetime.date.today().isocalendar()[1] % 2
    table = 'service.timetable_odd' if week else 'service.timetable_even'

    if message.text == "Понедельник" or message.text == "Вторник" or message.text == "Среда" or message.text == "Четверг" or message.text == "Пятница":
        try:

            cursor.execute(
                "SELECT subject, room_numb, start_time FROM {} WHERE day='{}'".format(table, message.text))
            result = cursor.fetchall()
            to_print = []
            for i in result:
                to_print.append(', '.join(i) + '\n')

            bot.send_message(message.chat.id, ''.join(to_print))
        except:
            bot.send_message(message.chat.id, 'Пар нет')



    elif message.text == 'Расписание на текущую неделю':
        to_print = []
        for day in days:
            cursor.execute(
                "SELECT subject, room_numb, start_time FROM {} WHERE day='{}'".format(table, day))
            result = cursor.fetchall()
            tmp = []
            tmp.append(day + '\n' + '_________\n')
            for i in result:
                tmp.append(', '.join(i) + '\n')
            to_print.append(''.join(tmp) + '\n')
        bot.send_message(message.chat.id, ''.join(to_print))

    elif message.text == 'Расписание на следующую неделю':
        to_print = []
        table = 'service.timetable_odd' if table == 'service.timetable_even' else 'service.timetable_even'
        for day in days:
            cursor.execute(
                "SELECT subject, room_numb, start_time FROM {} WHERE day='{}'".format(table, day))
            result = cursor.fetchall()
            tmp = []
            tmp.append(day + '\n' + '_________\n')
            for i in result:
                tmp.append(', '.join(i) + '\n')
            to_print.append(''.join(tmp) + '\n')
        table = 'service.timetable_odd' if table == 'service.timetable_even' else 'service.timetable_even'
        bot.send_message(message.chat.id, ''.join(to_print))


bot.polling()