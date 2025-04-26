import telebot
from telebot import types
import funcs_bot
import requests
import random, os
from telebot.handler_backends import ContinueHandling
# Замени 'TOKEN' на токен твоего бота
# Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("7988678579:AAHdVG6Jqlep-8tRS6_aIhj0gl_RBr-hXjM")


@bot.message_handler(commands=['start'])
def button(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("create password", callback_data="pass")
    item2 = types.InlineKeyboardButton("tell joke", callback_data="anekdot")
    item3 = types.InlineKeyboardButton("dog memes", callback_data="dog_memes")
    
    markup.add(item1, item2, item3, )
    bot.send_message(message.chat.id, "Выберите опцию:", reply_markup=markup)


@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == "pass":
            bot.send_message(call.message.chat.id, funcs_bot.parol()) 
              
        elif call.data == "anekdot":
            bot.send_message(call.message.chat.id, funcs_bot.anekdot())
        
        elif call.data == "dog_memes":
            bot.send_message(call.message.chat.id, funcs_bot.dog_memes())
        
        
    
@bot.message_handler(commands=['photo'])
def send_photo(message):
    file = random.choice(os.listdir("mems"))
    with open(f"mems\\{file}", "rb") as f:       
        bot.send_photo(message.chat.id, f)

bot.polling(non_stop=True)


