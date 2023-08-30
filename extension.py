import requests
import json
import telebot
from logger import logger
from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.path.dirname(__file__),'.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

bot = telebot.TeleBot(os.getenv('API_TOKEN'))

class ConvException(Exception):
    pass

class Converter:
    @staticmethod
    def convert(cur_1, cur_2, amount, message):

        try:
            r = requests.get(f'https://v6.exchangerate-api.com/v6/98b98fe068cd96349589f9f5/latest/{cur_1}')
        except ValueError:
            logger.info('Что-то пошло не так')
            bot.send_message(message.chat.id, 'Что-то пошло не так.')
            return

        try:
            result = float(json.loads(r.content)['conversion_rates'][str(cur_2).upper()])
        except Exception:
            logger.info('Введено некорректное наименование валюты.')
            bot.send_message(message.chat.id, 'Введите корректное наименование валюты.')
            return

        try:
            type(int(amount)) == int
        except ValueError:
            logger.info('Введено некорректное количество валюты')
            bot.send_message(message.chat.id, 'Введите корректное число валюты.')
            return

        text = (f'{amount} {cur_1.upper()} = {str(int(amount)*result)} {cur_2.upper()}')
        bot.send_message(message.chat.id, text)
