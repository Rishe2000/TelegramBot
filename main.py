import logging


import ApiFile
import DisplayText

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    ApplicationBuilder,
    CallbackQueryHandler,
    ContextTypes,
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    filters
)



logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

PHOTO, STYLE = range(2)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=DisplayText.INTRO_TEXT)

async def  begin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Sends a message with two inline buttons attached."""
    keyboard = [
        [InlineKeyboardButton("Create a sticker", callback_data="create_sticker")],
        [InlineKeyboardButton("List commands", callback_data="list_of_commands")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(DisplayText.PROVIDE_OPTION_TEXT, reply_markup=reply_markup)

async def beginStickerCreationText(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #always need to answer query before proceeding
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text=DisplayText.NAME_STICKER_SET_TEXT)




"""Start Sticker Creation Conversation"""

async def askForPhoto(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(text=DisplayText.UPLOAD_PICTURE_TEXT)
    return PHOTO

async def chooseStyle(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(text="You have chosen this image")
    await context.bot.sendPhoto(chat_id=update.effective_chat.id, photo="./src/Avatar_Photo.png")

    keyboard = [
        [InlineKeyboardButton("Kenga", callback_data="kenga")],
        [InlineKeyboardButton("Mau", callback_data="mau")],
        [InlineKeyboardButton("Anime", callback_data="anime")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(text=DisplayText.CHOOSE_STYLE_TEXT, reply_markup=reply_markup)
    return STYLE

async def displaySticker(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    styleReply = update.callback_query

    style = styleReply.data

    ApiFile.generateAvatar(style)

    await styleReply.answer()
    await context.bot.sendPhoto(chat_id=update.effective_chat.id, photo="./dest/generated_Avatar.png", caption="Looking good there mate!")
    return ConversationHandler.END

async def end(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancels and ends the conversation."""
    await update.message.reply_text(
        "Bye! Looking forward to more stickers from you!"
    )

    return ConversationHandler.END


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


"""End Sticker Creation Conversation"""

if __name__ == '__main__':
    teleBotToken = '6189330693:AAG_fRYjH9VvOJtnCa2OP3Qi2g-NNAZ7Unc'

    application = ApplicationBuilder().token(teleBotToken).build()

    #Command Handlers
    start_handler = CommandHandler('start', start)
    begin_handler = CommandHandler('begin', begin)
    create_sticker_handler = CommandHandler('createSticker', askForPhoto)
    photo_uploaded_handler = CommandHandler('done', chooseStyle)
    cancel_handler = CommandHandler("end", end)


    #CallbackQuery Handlers
    createSticker_button_handler = CallbackQueryHandler(callback=beginStickerCreationText, pattern="create_sticker")
    kenga_sticker_handler = CallbackQueryHandler(callback=displaySticker, pattern="kenga")
    mau_sticker_handler = CallbackQueryHandler(callback=displaySticker, pattern="mau")
    anime_sticker_handler = CallbackQueryHandler(callback=displaySticker, pattern="anime")

    #Message Handlers

    #Conversation Handlers
    create_sticker_conversation_hander = ConversationHandler(
        entry_points=[createSticker_button_handler],
        states = {
            PHOTO: [photo_uploaded_handler],
            STYLE: [kenga_sticker_handler, mau_sticker_handler, anime_sticker_handler],
        },
        fallbacks=[cancel_handler],

    )

    #Add Handlers
    application.add_handler(start_handler)
    application.add_handler(begin_handler)
    application.add_handler(create_sticker_handler)
    application.add_handler(createSticker_button_handler)
    application.add_handler(cancel_handler)
    application.add_handler(photo_uploaded_handler)
    application.add_handler(create_sticker_conversation_hander)
    application.add_handler(kenga_sticker_handler)
    application.add_handler(mau_sticker_handler)
    application.add_handler(anime_sticker_handler)

    application.run_polling()
