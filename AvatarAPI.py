"""
This is the API our telegram bot will use. Visit https://mirror-ai-api-docs.gitbook.io/mirror-ai-api/ to learn more.
There are certain requirements for the picture that needs to be uploaded. Please follow them strictly to ensure
ensure getting a successful response through the API.
"""

import requests

import Credentials


def generateAvatar(avatarStyle):

    """
    :param avatarStyle:
    :return: Success Code

    Took the CURL request from the API doc. Imported into Postman. Copied the generated python code from postman.
    """

    original_photo_filepath = "Users/rishebabu/Desktop/TLSCode/TelegramBot/src/Original_Photo.png"
    generated_avatar_filepath = "Users/rishebabu/Desktop/TLSCode/TelegramBot/dest/generated_Avatar.png"

    url = Credentials.MIRROR_API_URL + avatarStyle

    payload = {}
    files = [
        ('photo', ('Original_Photo.png', open(original_photo_filepath, 'rb'),
                   'image/png'))
    ]

    headers = {
        'X-Token': Credentials.MIRROR_API_TOKEN
    }

    avatarResponse = requests.request("POST", url, headers=headers, data=payload, files=files)

    avatarJsonResponse = avatarResponse.json()

    try:
        imageURL = avatarJsonResponse["face"]["url"]
    except:
        return 0
    else:
        generatedAvatar = requests.get(imageURL)
        with open(generated_avatar_filepath, "wb") as f:
            f.write(generatedAvatar.content)
        return 1
