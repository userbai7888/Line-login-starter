from flask import Flask, request, abort
import traceback
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
#======這裡是呼叫的檔案內容=====
from message import *
from new import *
from Function import *
from sushi import *
#======這裡是呼叫的檔案內容=====
#----------------------------import------------------------------------

app = Flask(__name__)
# Channel Access Token
line_bot_api = LineBotApi('p5M+z5sA0rK7XVnNsC1ctvNjuCqKhpqHpwt1b+h4KAI+JOPRRfTHT9IzcZRmrYykpNRRbPQ3oN6WxSW0zNS8Bja8uA9+fNSUgQ9/5yi065tPuM2brSTXgh/m80h6BUww5W/F1wZm5nfvwmukGZjP3QdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('028d41a891d0e0e2beaa764bfbf20c20')

# 监听所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("---------ERROR---------")
        abort(400)
    return 'OK'


# 处理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text.encode('utf-8').decode('utf-8')
    try:
        if msg in "我想購物":
            message = imagemap_message()
            line_bot_api.reply_message(event.reply_token, message)
        elif msg in '註冊按钮':
            message = buttons_message()
            #print(type(message))
            #print(message)
            line_bot_api.reply_message(event.reply_token, message)
        # 注册会员
        # elif '注册会员' in msg:
        #     message = Confirm_Template()
        #     line_bot_api.reply_message(event.reply_token, message)
        elif msg in '旋轉木馬產品':
            message = Carousel_Template()
            line_bot_api.reply_message(event.reply_token, message)


        elif msg in '圖片輪播圖':
            message = test()
            line_bot_api.reply_message(event.reply_token, message)
        elif msg in '功能簡介':
            message = function_list()
            print(message)
            line_bot_api.reply_message(event.reply_token, message)

        # elif '位置' in msg:
        #     message = LocationSendMessage(
        #         title='my location',
        #         address='Tokyo',
        #         latitude=35.65910807942215,
        #         longitude=139.70372892916203
        #     )
        #     line_bot_api.reply_message(event.reply_token, message)


        # elif "美食" in msg:
        #     message = send_sushi()
        #     print(type(message))
        #     print(message)
        #     line_bot_api.reply_message(event.reply_token, message)
        else:
            message = TextSendMessage(text="您輸入的有誤，請正確輸入。如：我想購物，產品列表等......")
            line_bot_api.reply_message(event.reply_token, message)
    except Exception as e:
        traceback.print_exc()
        print(e)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)








