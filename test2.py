if call.data == 'butt_idEn':
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
src = 'ru'