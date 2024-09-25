from telegram_bot import bot
from web_app.app import app


def main():
    bot.polling(none_stop=True)


if __name__ == '__main__':
    app.run(debug=True, host="https://129school.wuaze.com/", port=80)
    main()
