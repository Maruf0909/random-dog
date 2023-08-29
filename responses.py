from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import CallbackContext

from dog import dog_photo


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    # welcome message
    text = f"Hi {update.message.chat.first_name}! I'm a bot that can send random dog photos. \n\n" \
              f"send /dog to get a photo of a dog."

    # create dog button
    dog_button = KeyboardButton(text='dog')

    # create the keyboard
    keyboard = ReplyKeyboardMarkup(keyboard=[[dog_button]], resize_keyboard=True, one_time_keyboard=True)
    
    # send the message
    update.message.reply_text(text=text, reply_markup=keyboard)


def dog(update: Update, context: CallbackContext) -> None:
    """Send a random dog photo when the command /dog is issued."""
    # get the dog photo
    photo = dog_photo()
    
    # send the photo
    update.message.reply_photo(photo=photo)


def unknown(update: Update, context: CallbackContext) -> None:
    """Send a message when an unknown command is issued."""
    # send the message
    update.message.reply_text(text="Sorry, I didn't understand that command.")
