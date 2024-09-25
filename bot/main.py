from threading import Thread
from telegram_bot import bot
from web_app.app import app


def main():
    bot.polling(none_stop=True)


def running():
    app.run(debug=True)


if __name__ == '__main__':
    # t = Thread(target=running())
    # t.start()
    main()
