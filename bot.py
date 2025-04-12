import telebot
import funcs_bot
import logging
# Замени 'TOKEN' на токен твоего бота
# Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("token")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")
@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")



@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "Кнопка 1":
        bot.send_message(message.chat.id, "Вы нажали Кнопку 1!")
    elif message.text == "Кнопка 2":
        bot.send_message(message.chat.id, "Вы нажали Кнопку 2!")

if __name__ == "__main__":
    try:
        bot.polling(non_stop=True)
    except Exception as e:
        logging.error(f"Bot polling error: {e}")

