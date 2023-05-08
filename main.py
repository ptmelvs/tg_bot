import googletrans
import telebot
from telebot import types
from telebot.types import Message, CallbackQuery
from googletrans import Translator

translator = Translator()

avl_langs = ['EN🇬🇧', 'KO🇰🇷', 'ZH-CN🇨🇳', 'FR🇲🇫', 'DE🇩🇪']


def read_token() -> str:
    with open('token.txt', ) as file:
        token = file.read().removesuffix('\n')
        return token


API_TOKEN = read_token()
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['help'])
def help_command(message: Message):
    global src
    global dest
    src = 'ru'
    dest = 'ru'
    bot.send_message(message.chat.id, 'Доступные команды бота:\n/tolangs - Перевод с выбранного языка на '
                                      'русский\n/ru_oth - Перевод русского сообщения на выбранный язык')


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


@bot.message_handler(commands=['ru_oth'])
def ru_to_other(message):
    markup_ru = types.InlineKeyboardMarkup()
    buttonE = types.InlineKeyboardButton(text=avl_langs[0], callback_data='butt_idEn')
    buttonK = types.InlineKeyboardButton(text=avl_langs[1], callback_data='butt_idKo')
    buttonZC = types.InlineKeyboardButton(text=avl_langs[2], callback_data='butt_idZCh')
    buttonF = types.InlineKeyboardButton(text=avl_langs[3], callback_data='butt_idFr')
    buttonD = types.InlineKeyboardButton(text=avl_langs[4], callback_data='butt_idDe')

    markup_ru.add(buttonE, buttonK, buttonZC, buttonF, buttonD)

    bot.send_message(message.chat.id, 'Доступные языки для перевода:', reply_markup=markup_ru)


@bot.callback_query_handler(func=lambda call: True)
def check_callback(call: CallbackQuery):
    global dest
    global src
    src = 'ru'
    dest = 'ru'
    try:
        if call.data == 'butt_idE':
            bot.send_message(call.message.chat.id,
                             'Вы выбрали английский язык, введите слово или предложение на английском, которые вы хотите перевести')
            src = 'en'
        elif call.data == 'butt_idK':
            bot.send_message(call.message.chat.id,
                             'Вы выбрали корейский язык, введите слово или предложение на корейском, которые вы хотите перевести')
            src = 'ko'
        elif call.data == 'butt_idZC':
            bot.send_message(call.message.chat.id,
                             'Вы выбрали китайский язык, введите слово или предложение на китайском, которые вы хотите перевести')
            src = 'zh-cn'
        elif call.data == 'butt_idF':
            bot.send_message(call.message.chat.id,
                             'Вы выбрали французский язык, введите слово или предложение на французском, которые вы хотите перевести')
            src = 'fr'
        elif call.data == 'butt_idD':
            bot.send_message(call.message.chat.id,
                             'Вы выбрали немецкий язык, введите слово или предложение на немецком, которые вы хотите перевести')
            src = 'de'

        elif call.data == 'butt_idEn':
            bot.send_message(call.message.chat.id, 'Введите сообщение на русском для перевода на английский')
            dest = 'en'
        elif call.data == 'butt_idKo':
            bot.send_message(call.message.chat.id, 'Введите сообщение на русском для перевода на корейский')
            dest = 'ko'
        elif call.data == 'butt_idZCh':
            bot.send_message(call.message.chat.id, 'Введите сообщение на русском для перевода на китайский')
            dest = 'zh-cn'
        elif call.data == 'butt_idFr':
            bot.send_message(call.message.chat.id, 'Введите сообщение на русском для перевода на французский')
            dest = 'fr'
        elif call.data == 'butt_idDe':
            bot.send_message(call.message.chat.id, 'Введите сообщение на русском для перевода на немецкий')
            dest = 'de'
    except:
        bot.send_message(call.message.chat.id, 'Возникла непредвиденная ошибка')

@bot.message_handler(func=lambda m: True)
def translate_message(message):
    translated_text = translator.translate(message.text, src=src, dest=dest).text
    bot.send_message(message.chat.id, translated_text)


bot.polling(none_stop=True)
