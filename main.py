import googletrans
import telebot
from telebot import types
from telebot.types import Message
from googletrans import Translator

translator = Translator()
list_of_langs = list(googletrans.LANGUAGES)
avl_langs = ['EN🇬🇧', 'KO🇰🇷', 'ZH-CN🇨🇳', 'FR🇲🇫', 'DE🇩🇪']


def read_token() -> str:
    with open('C:\\Users\\ch991\\PycharmProjects\\tg_bot\\venv\\token.txt', ) as file:
        token = file.read().removesuffix('\n')
        return token


dest = 'ru'

API_TOKEN = read_token()
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['tolangs'])
def av_langs(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text=avl_langs[0], callback_data='butt_idE')
    button2 = types.InlineKeyboardButton(text=avl_langs[1], callback_data='butt_idK')
    button3 = types.InlineKeyboardButton(text=avl_langs[2], callback_data='butt_idZC')
    button4 = types.InlineKeyboardButton(text=avl_langs[3], callback_data='butt_idF')
    button5 = types.InlineKeyboardButton(text=avl_langs[4], callback_data='butt_idD')

    markup.add(button1, button2, button3, button4, button5)

    bot.send_message(message.chat.id, 'Доступные языки для перевода:', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def check_callback(call):
    global src
    if call.data == 'butt_idE':
        bot.send_message(call.message.chat.id, 'Вы выбрали английский язык, введите слово или предложение на английском, которые вы хотите перевести')
        src = 'en'
    elif call.data == 'butt_idK':
        bot.send_message(call.message.chat.id, 'Вы выбрали ко   рейский язык, введите слово или предложение на корейском, которые вы хотите перевести')
        src = 'ko'
    elif call.data == 'butt_idZC':
        bot.send_message(call.message.chat.id, 'Вы выбрали китайский язык, введите слово или предложение на китайском, которые вы хотите перевести')
        src = 'zh-cn'
    elif call.data == 'butt_idF':
        bot.send_message(call.message.chat.id, 'Вы выбрали французский язык, введите слово или предложение на французском, которые вы хотите перевести')
        src = 'fr'
    elif call.data == 'butt_idD':
        bot.send_message(call.message.chat.id, 'Вы выбрали немецкий язык, введите слово или предложение на немецком, которые вы хотите перевести')
        src = 'de'


@bot.message_handler(func=lambda m: True)
def translate_message(message):
    translated_text = translator.translate(message.text, src=src, dest=dest).text
    bot.send_message(message.chat.id, translated_text)


@bot.message_handler(commands=['help'])
def help_command():
    pass


bot.polling(none_stop=True)
print('\nБот завершил работу')
