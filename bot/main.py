from telegram_bot import bot
from database.database import database
from web_app.app import app


def main():
    bot.polling(none_stop=True)


if __name__ == '__main__':
    database.create_tables()
    main()
    app.run(debug=True)
