import os
import random

import requests
from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMessage


# 微信公众测试号ID和SECRET
app_id = os.environ["APP_ID"]
app_secret = os.environ["APP_SECRET"]

user_ids = os.environ["USER_ID"].split(',')
template_id = os.environ["WATER_TEMPLATE_ID"]


def get_push_content():
    words = requests.get("https://api.shadiao.pro/chp")
    if words.status_code != 200:
        return get_push_content()
    return words.json()['data']['text']


def get_random_color():
    return "#%06x" % random.randint(0, 0xFFFFFF)


chp = get_push_content()

client = WeChatClient(app_id, app_secret)

data = {
    "chp": {"value": chp, "color": get_random_color()}
}
for i in range(len(user_ids)):
    wm = WeChatMessage(client)
    result = wm.send_template(user_ids[i], template_id, data)
    print(result)
