import telebot
bot = telebot.TeleBot('905167223:AAFQQgfJjx8T5PdcWxkgzn4YNR9W4U1xyJw')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text == 'Пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')
    elif message.text == 'Арсении даун?':
        bot.send_message(message.chat.id, '++, ofc yes')

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)


bot.polling()