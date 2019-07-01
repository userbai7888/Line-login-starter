from flask import Flask, request, abort
import traceback
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.exceptions import LineBotApiError
from linebot.models import *
import requests
app = Flask(__name__)
#line_bot_api = LineBotApi('p5M+z5sA0rK7XVnNsC1ctvNjuCqKhpqHpwt1b+h4KAI+JOPRRfTHT9IzcZRmrYykpNRRbPQ3oN6WxSW0zNS8Bja8uA9+fNSUgQ9/5yi065tPuM2brSTXgh/m80h6BUww5W/F1wZm5nfvwmukGZjP3QdB04t89/1O/w1cDnyilFU=')
line_bot_api = LineBotApi('p5M+z5sA0rK7XVnNsC1ctvNjuCqKhpqHpwt1b+h4KAI+JOPRRfTHT9IzcZRmrYykpNRRbPQ3oN6WxSW0zNS8Bja8uA9+fNSUgQ9/5yi065tPuM2brSTXgh/m80h6BUww5W/F1wZm5nfvwmukGZjP3QdB04t89/1O/w1cDnyilFU=')


# 获取 rich menu id
def Rich_menu_id():
    rich_menu_to_create = RichMenu(
        size=RichMenuSize(width=2500, height=843),
        selected=False,
        name="Nice richmenu",
        chat_bar_text="Tap here",
        areas=[RichMenuArea(
            bounds=RichMenuBounds(x=0, y=0, width=2500, height=843),
            action=URIAction(label='Go to line.me', uri='https://line.me'))]
    )
    rich_menu_id = line_bot_api.create_rich_menu(rich_menu=rich_menu_to_create)
    print(rich_menu_id)
    return rich_menu_id
#上传rich menu
def upload_menu():
    with open( r"F:/Line-login-starter/uplodimg/richimg.jpg", 'rb') as f:
        upload = line_bot_api.set_rich_menu_image(Rich_menu_id(), "image/png", f)
    print(upload)
# 下载rich menu
def download_menu():
    content = line_bot_api.get_rich_menu_image(Rich_menu_id(),timeout=5)
    print(content)
    with open(r"F:/Line-login-starter/uplodimg/richimg1.jpg", 'wb') as fd:
        for chunk in content.iter_content():
            fd.write(chunk)
# 获取rich menu 列表
def get_menu_list():
    rich_menu_list = line_bot_api.get_rich_menu_list()
    for list in rich_menu_list:
        print(list)
    print(len(rich_menu_list))
    return rich_menu_list
# 获取rich menu
def get_menu():
    rich_menu = line_bot_api.get_rich_menu(Rich_menu_id())
    print(rich_menu)
    return rich_menu
# 删除 rich menu
def delete_menu():
    rich_menu = line_bot_api.delete_rich_menu(Rich_menu_id())
    print(rich_menu)
if __name__ == '__main__':
    #Rich_menu()
    #upload_menu()
    download_menu()
    #get_menu()

