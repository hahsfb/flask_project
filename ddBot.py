import requests

DINGDING_MESSAGE = 'https://oapi.dingtalk.com/robot/send?access_token=e7eee758ba35c26681c215ac650f972b95614ade270e6984f5e2759310ab9ea6'


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
