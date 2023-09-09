"""
These are the functions that get executed for each of the handlers called
"""

import DisplayText
import ApiFile

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    ContextTypes,
    ConversationHandler,
)

PHOTO, STYLE, FINAL = range(3)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=DisplayText.PROGRAM_START_TEXT)

async def  begin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Sends a message with two inline buttons attached."""
    keyboard = [
        [InlineKeyboardButton("Create a sticker", callback_data="create_sticker")],
        [InlineKeyboardButton("List commands", callback_data="list_of_commands")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(DisplayText.CHOOSE_STICKER_BUTTON_TEXT, reply_markup=reply_markup)


async def listCommands(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=DisplayText.LIST_COMMAND_TEXT)





"""Start Sticker Creation Conversation"""

async def askForPhoto(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    #always need to answer query before proceeding
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text=DisplayText.ASK_FOR_STYLE_TEXT)
    return PHOTO

async def askForPhotoAgain(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(DisplayText.ASK_FOR_STYLE_TEXT)


async def askForStyle(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:

    try:
        await update.message.reply_text(text="You have chosen this image")
        await context.bot.sendPhoto(chat_id=update.effective_chat.id, photo="./src/Original_Photo.png")
    except:
        await update.message.reply_text(text=DisplayText.IMAGE_UPLOAD_FAILURE_TEXT)
        return PHOTO
    else:
        keyboard = [
            [InlineKeyboardButton("Kenga", callback_data="kenga")],
            [InlineKeyboardButton("Mau", callback_data="mau")],
            [InlineKeyboardButton("Anime", callback_data="anime")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text(text=DisplayText.CHOOSE_STYLE_TEXT, reply_markup=reply_markup)
        return STYLE


async def generateAvatar(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    style = query.data
    await query.answer()

    apiSuccess = ApiFile.generateAvatar(style)

    if apiSuccess:
        await context.bot.sendPhoto(chat_id=update.effective_chat.id, photo="./dest/generated_Avatar.png",
                                    caption=DisplayText.API_SUCCESS_TEXT)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=DisplayText.CHOOSE_CREATE_OR_END_STICKER)
        return FINAL
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=DisplayText.API_FAILURE_TEXT)
        return STYLE



async def end(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancels and ends the conversation."""

    await update.message.reply_text(text=DisplayText.END_TEXT)
    return ConversationHandler.END



"""
Experiment on how instead of pre-setting the name and location of the file, we can send any picture from our phone or laptop 
to the telegram chat and it will return us the avatar. Enhances user experience.
"""


# async def photo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
#     """Stores the photo and asks for a location."""
#     user = update.message.from_user
#     photo_file = await update.message.photo[-1].get_file()
#     await photo_file.download_to_drive("user_photo.jpg")
#     logger.info("Photo of %s: %s", user.first_name, "user_photo.jpg")
#     await update.message.reply_text(
#         "Gorgeous! Now, send me your location please, or send /skip if you don't want to."
#     )
#
#     return LOCATION
