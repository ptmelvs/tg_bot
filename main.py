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

src = ''
dest = ''

API_TOKEN = read_token()
bot = telebot.TeleBot(API_TOKEN)
@bot.message_handler(commands=['tolangs'])
def av_langs(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text=avl_langs[0], callback_data='butt_id')
    button2 = types.InlineKeyboardButton(text=avl_langs[1], callback_data='butt_id')
    button3 = types.InlineKeyboardButton(text=avl_langs[2], callback_data='butt_id')
    button4 = types.InlineKeyboardButton(text=avl_langs[3], callback_data='butt_id')
    button5 = types.InlineKeyboardButton(text=avl_langs[4], callback_data='butt_id')

    markup.add(button1, button2, button3, button4, button5)

    bot.send_message(message.chat.id, 'Доступные языки для перевода:', reply_markup=markup)


@bot.message_handler(func=lambda m: True)
def translate_message(message):
    translated_text = translator.translate(message.text, src=src, dest=dest).text
    bot.send_message(message.chat.id, translated_text)


@bot.message_handler(commands=['help'])
def help_command():
    pass


bot.polling(none_stop=True)
print('\nБот завершил работу')
