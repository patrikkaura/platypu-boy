import requests
import names
import datetime
import os

API_URI = "https://gate.whapi.cloud/messages/image"
API_TOKEN = os.environ.get("BOT_API_TOKEN")
IMAGE_BASE_URI = (
    "https://raw.githubusercontent.com/patrikkaura/platypus-bot/master/images"
)
RECEIVER_ADDRESS = os.environ.get("BOT_RECEIVER_ADDRESS")


def _get_day_number_prefixed_with_zero():
    """
    Get day number prefixed with zero. For example 02 for second day of the month.
    :return:
    """
    day_number = datetime.datetime.now().day
    return f"{day_number:02}"


def send_whatsapp_message():
    """
    Send a request to whapi.cloud API with whatsapp message with platypus image
    stored in github repo.
    :return:
    """
    print(API_TOKEN)
    print(API_URI)
    print(RECEIVER_ADDRESS)

    name = names.get_first_name("male")
    message = f"Welcome to Platypus Daily, your daily dose of platypus. This is Platypus {name}. Say hi to {name}!"
    index = _get_day_number_prefixed_with_zero()

    response = requests.post(
        API_URI,
        json={
            "media": f'{IMAGE_BASE_URI}/{index}.jpeg',
            "to": RECEIVER_ADDRESS,
            "caption": message,
        },
        headers={
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": f"Bearer {API_TOKEN}",
        },
    )

    print(response)


if __name__ == "__main__":
    send_whatsapp_message()
