from telegram.ext import ApplicationBuilder
import logging

import Credentials
import Handlers

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def main():

    application = ApplicationBuilder().token(Credentials.TELEGRAM_BOT_TOKEN).build()

    for handler in Handlers.HANDLER_LIST:
        application.add_handler(handler)
    application.run_polling()


if __name__ == '__main__':
    main()
