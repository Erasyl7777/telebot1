import telebot
import funcs_bot
# Замени 'TOKEN' на токен твоего бота
# Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("7988678579:AAHdVG6Jqlep-8tRS6_aIhj0gl_RBr-hXjM")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")
@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")



@bot.message_handler(content_types=["text"])
def handle_message(message):
    if message.text.lower == "расскажи анекдот" or  "раскажи анекдот":
        bot.send_message(message.chat.id, funcs_bot.anekdot() )

@bot.message_handler(content_types=["text"])
def send_hello(message):
    if message.text.lower == "hello" or  "привет":
        bot.send_message(message.chat.id, f"привет, {message.from_user.first_name}")

bot.polling(non_stop=True)