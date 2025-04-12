import telebot
from telebot import types
import funcs_bot
import logging
from telebot.handler_backends import ContinueHandling
# Замени 'TOKEN' на токен твоего бота
# Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("7988678579:AAHdVG6Jqlep-8tRS6_aIhj0gl_RBr-hXjM")

@bot.message_handler(commands=['start'])
def button(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("create password", callback_data="pass")
    item2 = types.InlineKeyboardButton("tell joke", callback_data="anekdot")
    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Выберите опцию:", reply_markup=markup)
@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == "pass":
            bot.send_message(call.message.chat.id, funcs_bot.parol()) 
              
        elif call.data == "anekdot":
            bot.send_message(call.message.chat.id, funcs_bot.anekdot())
bot.polling(non_stop=True)

