from telegram import Update
from telegram.ext import CallbackContext

from dog import dog_photo


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    # welcome message
    text = f"Hi {update.message.chat.first_name}! I'm a bot that can send random dog photos. \n\n" \
              f"send /dog to get a photo of a dog."
    
    # send the message
    update.message.reply_text(text)


def dog(update: Update, context: CallbackContext) -> None:
    """Send a random dog photo when the command /dog is issued."""
    # get the dog photo
    photo = dog_photo()
    
    # send the photo
    update.message.reply_photo(photo=photo)
