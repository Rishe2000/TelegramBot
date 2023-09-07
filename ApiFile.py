import requests
def generateAvatar(avatarStyle):
    url = "https://public-api.mirror-ai.net/v2/generate?style=" + avatarStyle
    mirrorAItoken = '11620a0ae0e540a7b8145db01865c5fc'
    # file_location = ""

    payload = {}
    files = [
        ('photo', ('Avatar_Photo.png', open('./src/Avatar_Photo.png', 'rb'),
                   'image/png'))
    ]

    headers = {
        'X-Token': mirrorAItoken
    }

    avatarResponse = requests.request("POST", url, headers=headers, data=payload, files=files)

    avatarJsonResponse = avatarResponse.json()

    imageURL = avatarJsonResponse["face"]["url"]
    generatedAvatar = requests.get(imageURL)
    with open("./dest/generated_Avatar.png", "wb") as f:
        f.write(generatedAvatar.content)

    return imageURL
