from telegram_bot import bot
from database.database import database
from web_app.app import app


def main():
    bot.polling(none_stop=True)


database.create_tables()
main()
