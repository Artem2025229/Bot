import telebot
import random

bot = telebot.TeleBot("7630638761:AAH6nzRJRK7_c4in7-Iv2xwwWGcq-_MQuo")

# Словарь для команды /video
videos = {
    "Что из себя представляет вселенная": "https://www.youtube.com/watch?v=V63UrLL7Avs",
    "Мемы": "https://www.youtube.com/watch?v=kZmm30pBlJY",
    "Как картели варят наркотики": "https://www.youtube.com/watch?v=kdcxkmMoVV4&t"
    "История доллара": "https://www.youtube.com/watch?v=oHqlOyjFAqw"
    "История подделки денег": "https://www.youtube.com/watch?v=YViF19tE8fA&t"
    "История видеоигр": "https://www.youtube.com/watch?v=fws1b2uFKV8" 
}




@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Для вывода всех команд напиши /help!")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['help'])
def send_help(message):
    commands_list = (
        "/start - Начать работу с ботом"
        "/hello - Сказать 'Привет"
        "/bye - Попрощаться"
        "/help - Показать список команд"
        "/coin - Играть в орёл или решка"
        "/video - Получить случайное видео из списка"
    )
    bot.reply_to(message, f"Список команд:{commands_list}")

@bot.message_handler(commands=['coin'])
def flip_coin(message):
    outcome = random.choice(["Орёл", "Решка"])
    bot.reply_to(message, f"Выпало: {outcome}")

@bot.message_handler(commands=['video'])
def send_video(message):
    video_name, video_link = random.choice(list(videos.items()))
    bot.reply_to(message, f"Вот тебе видео:{video_name}Ссылка: {video_link}")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

print('Бот запущен!')
bot.polling()
