from telegram_bot import bot
from School129_bot.database.database import database


def main():
    bot.polling(none_stop=True)


if __name__ == '__main__':
    database.create_tables()
    main()