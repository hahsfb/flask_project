import requests
from app.setting import DINGDING_MESSAGE


def seng_message_dingding(title):
    data = {
         "msgtype": "text",
         "text": {
             "content": title
         }
     }
    requests.post(DINGDING_MESSAGE, json=data)


if __name__ == "__main__":
    seng_message_dingding('title')
