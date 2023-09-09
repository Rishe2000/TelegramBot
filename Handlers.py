"""
This file contains the different handlers (Command Handlers, Conversation Handler, CallBackQuery Handlers...)
"""

import Functions

from telegram.ext import (
    CallbackQueryHandler,
    CommandHandler,
    ConversationHandler,
)



PHOTO, STYLE, FINAL = range(3)

# Command Handlers
start_command_handler = CommandHandler('start', Functions.start)
begin_command_handler = CommandHandler('begin', Functions.begin)
choose_avatar_style_command_handler = CommandHandler('AvatarStyle', Functions.askForStyle)
upload_photo_again_command_handler = CommandHandler('uploadPhotoAgain', Functions.askForStyle)
create_new_sticker_again_command_handler = CommandHandler('createNewStickerAgain', Functions.askForPhotoAgain)
end_program_command_handler = CommandHandler("end", Functions.end)
cancel_command_handler = CommandHandler("cancel", Functions.end)

# CallbackQuery Handlers
clicked_create_a_sticker_button = CallbackQueryHandler(callback=Functions.askForPhoto, pattern="create_sticker")
clicked_list_command_button = CallbackQueryHandler(callback=Functions.listCommands, pattern="list_of_commands")
clicked_kenga_button = CallbackQueryHandler(callback=Functions.generateAvatar, pattern="kenga")
clicked_mau_button = CallbackQueryHandler(callback=Functions.generateAvatar, pattern="mau")
clicked_anime_button = CallbackQueryHandler(callback=Functions.generateAvatar, pattern="anime")

# Conversation Handler

create_sticker_conversation_handler = ConversationHandler(

    entry_points=[clicked_create_a_sticker_button, create_new_sticker_again_command_handler],
    states={
        PHOTO: [choose_avatar_style_command_handler, upload_photo_again_command_handler],
        STYLE: [clicked_kenga_button, clicked_mau_button, clicked_anime_button],
        FINAL: [create_new_sticker_again_command_handler, end_program_command_handler],
    },
    fallbacks=[cancel_command_handler],

)

HANDLER_LIST = [
    start_command_handler,
    begin_command_handler,
    clicked_list_command_button,
    create_sticker_conversation_handler
]