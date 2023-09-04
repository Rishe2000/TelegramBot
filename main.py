import logging

import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CallbackQueryHandler, ContextTypes, CommandHandler

import ApiFile
import DisplayText

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=DisplayText.START_TEXT)

async def  clickedYes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=DisplayText.STYLE_TEXT)

async def wantKenga(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ApiFile.generateAvatar("kenga")
    await context.bot.send_message(chat_id=update.effective_chat.id, text=DisplayText.CHECK_IMAGE_TEXT)


async def wantMau(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ApiFile.generateAvatar("mau")
    await context.bot.send_message(chat_id=update.effective_chat.id, text=DisplayText.CHECK_IMAGE_TEXT)

async def wantAnime(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ApiFile.generateAvatar("anime")
    await context.bot.send_message(chat_id=update.effective_chat.id, text=DisplayText.CHECK_IMAGE_TEXT)



if __name__ == '__main__':
    teleBotToken = '6189330693:AAG_fRYjH9VvOJtnCa2OP3Qi2g-NNAZ7Unc'

    application = ApplicationBuilder().token(teleBotToken).build()

    start_handler = CommandHandler('start', start)
    yes_handler = CommandHandler('yes', clickedYes)
    kenga_handler = CommandHandler('kenga', wantKenga)
    mau_handler = CommandHandler('mau', wantMau)
    anime_handler = CommandHandler('anime', wantAnime)

    application.add_handler(start_handler)
    application.add_handler(yes_handler)
    application.add_handler(kenga_handler)
    application.add_handler(mau_handler)
    application.add_handler(anime_handler)

    application.run_polling()
    # print(telegram.Bot.base_url)

