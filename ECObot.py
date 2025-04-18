import telebot

bot = telebot.TeleBot("TOKEN")

#Словари

Москва = {
        "Пункт 1": "Адрес 1",
        "Пункт 2": "Адрес 2",
        "Пункт 3": "Адрес 3",
    }
Варшава = {
        "Пункт 1": "Адрес 1",
        "Пункт 2": "Адрес 2",
        "Пункт 3": "Адрес 3",
    }
Киев = {
        "Пункт 1": "Адрес 1",
        "Пункт 2": "Адрес 2",
        "Пункт 3": "Адрес 3",
    }
Прага = {
        "Пункт 1": "Адрес 1",
        "Пункт 2": "Адрес 2",
        "Пункт 3": "Адрес 3",
    }
Берлин = {
        "Пункт 1": "Адрес 1",
        "Пункт 2": "Адрес 2",
        "Пункт 3": "Адрес 3",
    }

Минск = {
        "Пункт 1": "Адрес 1",
        "Пункт 2": "Адрес 2",
        "Пункт 3": "Адрес 3",
    }
Вашингтон = {
        "Пункт 1": "Адрес 1",
        "Пункт 2": "Адрес 2",
        "Пункт 3": "Адрес 3",
    }

#Код

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Этот бот показывает пункты приёа и переработки мусора в вашем городе.  Для вывода всех комманд напишите /help")

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to[message,'''/start - начать чат
                            /help - помощь
                            /cities - список городов
                        ''']

@bot.message_handler(commands=['cities'])
def send_welcome(message):
    bot.reply_to[message,'''/Москва
                            /Киев
                            /Варшава
                            /Прага
                            /Берлин
                            /Минск
                            /Вашингтон
                        ''']

@bot.message_handler(commands=['Москва'])
def send_welcome(message):
    bot.reply_to[message, Москва]

@bot.message_handler(commands=['Киев'])
def send_welcome(message):
    bot.reply_to[message, Киев]

@bot.message_handler(commands=['Варшава'])
def send_welcome(message):
    bot.reply_to[message, Варшава]

@bot.message_handler(commands=['Прага'])
def send_welcome(message):
    bot.reply_to[message, Прага]

@bot.message_handler(commands=['Берлин'])
def send_welcome(message):
    bot.reply_to[message, Берлин]

@bot.message_handler(commands=['Минск'])
def send_welcome(message):
    bot.reply_to[message, Минск]

@bot.message_handler(commands=['Вашингтон'])
def send_welcome(message):
    bot.reply_to[message, Вашингтон]

print('старт')
bot.polling()
