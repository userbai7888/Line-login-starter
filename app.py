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
line_bot_api = LineBotApi('J25/NaQfM/brcEm//lmChZoeTvU8h3QkCNMBYsFKwAVNb2cS+ZfmOF6/k7uTShdcpNRRbPQ3oN6WxSW0zNS8Bja8uA9+fNSUgQ9/5yi065sLRDRrQINV/Xkj8vH5NgqsLRGBdlX6WjVGL9DS7pCn5wdB04t89/1O/w1cDnyilFU=')
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
        if msg in "我想购物":
        #if '合作商' in msg:
            message = imagemap_message()
            line_bot_api.reply_message(event.reply_token, message)
        elif '最新消息' in msg:
            message = buttons_message()
            line_bot_api.reply_message(event.reply_token, message)
        # 注册会员
        # elif '注册会员' in msg:
        #     message = Confirm_Template()
        #     line_bot_api.reply_message(event.reply_token, message)
        elif '旋转木马' in msg:
            message = Carousel_Template()
            line_bot_api.reply_message(event.reply_token, message)


        elif '图片' in msg:
            message = test()
            line_bot_api.reply_message(event.reply_token, message)
        # elif '功能列表' in msg:
        #     message = function_list()
        #     line_bot_api.reply_message(event.reply_token, message)
        elif "美食" in msg:
            message = send_sushi()
            line_bot_api.reply_message(event.reply_token, message)

        
        else:
            message = TextSendMessage(text=msg)
            line_bot_api.reply_message(event.reply_token, message)
    except Exception as e:
        traceback.print_exc()
        print(e)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


