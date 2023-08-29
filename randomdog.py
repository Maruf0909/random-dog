# importing the required libraries for env variables
from dotenv import load_dotenv
import os

# import the required libraries for the bot
from telegram.ext import (
    Updater,
    CommandHandler,
    Dispatcher,
)

# import the handlers
from responses import (
    start,
    dog,
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
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("dog", dog))


    # start the bot
    updater.start_polling()
    # stop the bot
    updater.idle()


if __name__ == "__main__":
    main()