import requests

def generateAvatar(avatarStyle):
    url = "https://public-api.mirror-ai.net/v2/generate?style=" + avatarStyle
    mirrorAItoken = '11620a0ae0e540a7b8145db01865c5fc'
    # file_location = ""

    payload = {}
    files = [
        ('photo', ('rishe_photo.JPG', open('/Users/rishebabu/Desktop/Personal/rishe_photo.JPG', 'rb'),
                   'image/png'))
    ]
    headers = {
        'X-Token': mirrorAItoken
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    API_Data = response.json()

    image_url = API_Data["face"]["url"]
    response = requests.get(image_url)
    with open("RisheAvatar.jpg", "wb") as f:
        f.write(response.content)
