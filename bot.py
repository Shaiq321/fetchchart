import os

import telebot

BOT_TOKEN = "7160785140:AAHj-EdLG72nSdOtAmaP5SHzFdHF86RgIWg"

bot = telebot.TeleBot(BOT_TOKEN)
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()
   

