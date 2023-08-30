import telebot
from extension import Converter
from logger import logger
from dotenv import load_dotenv
import os


dotenv_path = os.path.join(os.path.dirname(__file__),'.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

bot = telebot.TeleBot(os.getenv('API_TOKEN'))

logger.info('Бот запущен')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    logger.info('Введена команда /start')
    bot.send_message(
        message.chat.id, 'Привет! Я умею конвертировать валюты из одной в другую!')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(
        message.chat.id, '''Чтобы скновертировать валюту, отправьте боту сообщение в формате <имя валюты, цену которой он хочет узнать>
        <имя валюты, в которой надо узнать цену первой валюты> <количество первой валюты>.''')


@bot.message_handler(content_types=['text'])
def result(message):
    values = message.text.split(' ')

    try:
        cur_1, cur_2, amount = values
    except ValueError:
        bot.send_message(
            message.chat.id, 'Введите нужное количество параметров.')
        return
    cur_1, cur_2, amount = values
    Converter.convert(cur_1, cur_2, amount, message)


bot.infinity_polling()
