from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = '7964468262:AAFWpwQ0stF5cNX6ZDO_1T7aBljKyib-B7E'
URL = f'https://api.telegram.org/bot{TOKEN}/'

def send_message(chat_id, text, reply_markup=None):
    data = {
        'chat_id': chat_id,
        'text': text,
        'reply_markup': reply_markup
    }
    requests.post(URL + 'sendMessage', json=data)

@app.route('/', methods=['POST'])
def webhook():
    data = request.json
    chat_id = data['message']['chat']['id']
    text = data['message'].get('text', '')

    if text == '/menu':
        keyboard = {
            "keyboard": [
                [{"text": "Opção 1"}, {"text": "Opção 2"}],
                [{"text": "Ajuda"}]
            ],
            "resize_keyboard": True,
            "one_time_keyboard": False
        }
        send_message(chat_id, "Escolha uma opção:", reply_markup=keyboard)
    else:
        send_message(chat_id, "Você digitou: " + text)

    return 'ok'
from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = 'COLE_SEU_TOKEN_AQUI'
URL = f'https://api.telegram.org/bot{TOKEN}/'

def send_message(chat_id, text, reply_markup=None):
    data = {
        'chat_id': chat_id,
        'text': text,
        'reply_markup': reply_markup
    }
    requests.post(URL + 'sendMessage', json=data)

@app.route('/', methods=['POST'])
def webhook():
    data = request.json
    chat_id = data['message']['chat']['id']
    text = data['message'].get('text', '')

    if text == '/menu':
        keyboard = {
            "keyboard": [
                [{"text": "Opção 1"}, {"text": "Opção 2"}],
                [{"text": "Ajuda"}]
            ],
            "resize_keyboard": True,
            "one_time_keyboard": False
        }
        send_message(chat_id, "Escolha uma opção:", reply_markup=keyboard)
    else:
        send_message(chat_id, "Você digitou: " + text)

    return 'ok'

