from flask import Flask, request, abort
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
#======這裡是呼叫的檔案內容=====

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('LzLBHYa0PSecqYXOmYrhXsed0k0e1Eh6fHYUBVsCw29MeM3 / c18YyPZqHPlXFIRYpNRRbPQ3oN6WxSW0zNS8​​Bja8uA9 + fNSUgQ9 / 5yi065udOSXyml9lUaUPzVlUd3dsqvOgv6Yf7wGFPyzUxcdxwAdB04t89 / 1O / w1cDnyilFU =')
# Channel Secret
handler = WebhookHandler('028d41a891d0e0e2beaa764bfbf20c20')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    print("你好，白先生！！！！")
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    print(signature)
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print(event)
    msg = event.message.text
    print(msg,"-"*100)
    if '你好' in msg:
        message = imagemap_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '最新活動訊息' in msg:
        message = buttons_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '註冊會員' in msg:
        message = Confirm_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '旋轉木馬' in msg:
        message = Carousel_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '圖片畫廊' in msg:
        message = test()
        line_bot_api.reply_message(event.reply_token, message)
    elif '功能列表' in msg:
        message = function_list()
        line_bot_api.reply_message(event.reply_token, message)
    else:
        message = TextSendMessage(text=msg)
        line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


