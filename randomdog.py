# importing the required libraries for env variables
from dotenv import load_dotenv
import os

# import the required libraries for the bot
from telegram.ext import (
    Updater,
    CommandHandler,
    Dispatcher,
    MessageHandler,
    Filters,
)

# import the handlers
from responses import (
    start,
    dog,
    unknown,
)

# load the .env file
load_dotenv()
# get the token from the .env file
TOKEN = os.getenv("TOKEN")

# create an Updater object
updater: Updater = Updater(token=TOKEN)

# create a dispatcher object
dispatcher: Dispatcher = updater.dispatcher


def main():
    # add the handlers to the dispatcher
    dispatcher.add_handler(handler=CommandHandler(command=('start', 'boshlash'), callback=start))
    dispatcher.add_handler(handler=MessageHandler(filters=(~Filters.text('dog') & Filters.text), callback=unknown))
    dispatcher.add_handler(handler=MessageHandler(filters=Filters.text('dog'), callback=dog))
    # dispatcher.add_handler(handler=MessageHandler(filters=Filters.photo, callback=dog))

    # start the bot
    updater.start_polling()
    # stop the bot
    updater.idle()


if __name__ == "__main__":
    main()