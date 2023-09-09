"""
This is the list of messages that will be sent by the telegram bot. The messages are separated to ensure a cleaner
looking code. We can also just change the messages here without disturbing the other parts of the files if we need
to in the future.
"""


PROGRAM_START_TEXT = "Welcome to Avatar Creator Bot!\nPress /begin to start generating avatars!"

CHOOSE_STICKER_BUTTON_TEXT = "Choose one of the options below"

LIST_COMMAND_TEXT = """
/start - Bot starts and introduces itself\n
/begin - Bot begins conversation to generate avatar\n
/AvatarStyle - Bot asks you to choose the style of your avatar\n
/uploadPhotoAgain - Bot asks you to upload photo again\n
/createNewStickerAgain - Bot will create another sticker for you\n
/end - Last step to end convo with bot\n
/cancel - Press anytime to cancel conversation with bot\n\n\n
Press /begin again to explore more!
"""

ASK_FOR_STYLE_TEXT = """
These are the requirements for the photo you upload:\n 

1.The image should be in *PNG* or *JPG* formats.\n
2.The maximum size of the image should not exceed 2340 pixels on any side.\n
3.Maximum product of the width and height of the image in pixels should not exceed 5,000,000.\n

After preparing your photo, save the picture in your \"src\" folder.
Now press /AvatarStyle to choose your avatar's style!
"""

IMAGE_UPLOAD_FAILURE_TEXT = """
There might be issues with the picture you saved. Kindly check for these requirements again:\n\n

1.Image is of either *PNG* or *JPG* format\n
2.Image is named either \"Avatar_Photo.png\" or \"Avatar_Photo.jpg\"\n
3.Image is stored in the src folder\n\n

Once you have checked these requirements, upload your photo again by pressing /uploadPhotoAgain.
"""

API_SUCCESS_TEXT = "Looking good there mate!"

API_FAILURE_TEXT = """
Your image could not be uploaded :(( Please check if your image adheres to these requirements: \n\n

1.The image should be in *PNG* or *JPG* formats.\n
2.The maximum size of the image should not exceed 2340 pixels on any side.\n
3.Maximum product of the width and height of the image in pixels should not exceed 5,000,000.\n

Once you have prepard your photo, press /createSticker to begin!
"""

CHOOSE_STYLE_TEXT = "Please choose a style:\n1.Kenga\n2.Mau\n3.Anime"

CHOOSE_CREATE_OR_END_STICKER = """
If you want to create a new sticker, click /createNewStickerAgain. If you are done, click /end"
"""

END_TEXT = "Bye! Looking forward to more stickers from you!"