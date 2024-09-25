from config.config import bot_config, logger
from database.database import Database
import telebot

bot = telebot.TeleBot(bot_config['bot_token'])

database = Database()
database.create_tables()

def check_registration(message):
    if not database.check_registration(message.from_user.id):
        return False
    return True


@bot.message_handler(commands=['start'])
def send_welcome(message):
    if not check_registration(message):
        database.add_user(message.from_user.id, message.from_user.username)
        logger.info(f"User {message.from_user.username} ({message.from_user.id}) added to standings")
        bot.send_message(message.chat.id, "Я тебя зарегистрировал")
    else:
        logger.info(f"User {message.from_user.username} ({message.from_user.id}) tried to start again")
        bot.send_message(message.chat.id, "Ты уже зарегистрирован")


@bot.message_handler(commands=['help'])
def help(message):
    if not check_registration(message):
        bot.send_message(message.chat.id, "Сначала зарегистрируйся: /start")
        logger.info(f"User {message.from_user.username} ({message.from_user.id}) is not registered")
        return

    bot.send_message(message.chat.id, "Чтобы начать тапать, напиши /tap")
    logger.info(f"User {message.from_user.username} ({message.from_user.id}) asked for help")


@bot.message_handler(commands=['tap'])
def tap(message):
    if not check_registration(message):
        bot.send_message(message.chat.id, "Сначала зарегистрируйся: /start")
        logger.info(f"User {message.from_user.username} ({message.from_user.id}) is not registered")
        return

    current_balance = database.get_balance(message.from_user.id)
    current_balance += 1
    bot.send_message(message.chat.id, f"Тап! Баланс: {current_balance}")
    logger.info(f"User {message.from_user.username} ({message.from_user.id}) tapped")

    database.update_balance(message.from_user.id, current_balance)

@bot.message_handler(commands=['stats'])
def stats(message):
    if not check_registration(message):
        bot.send_message(message.chat.id, "Сначала зарегистрируйся: /start")
        logger.info(f"User {message.from_user.username} ({message.from_user.id}) is not registered")
        return

    # standings =
    # bot.send_message(message.chat.id, "Текущие балансы : " + )
