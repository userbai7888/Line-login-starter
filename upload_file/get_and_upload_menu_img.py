import requests
import json
from linebot import (
    LineBotApi, WebhookHandler
)
line_bot_api = LineBotApi('p5M+z5sA0rK7XVnNsC1ctvNjuCqKhpqHpwt1b+h4KAI+JOPRRfTHT9IzcZRmrYykpNRRbPQ3oN6WxSW0zNS8Bja8uA9+fNSUgQ9/5yi065tPuM2brSTXgh/m80h6BUww5W/F1wZm5nfvwmukGZjP3QdB04t89/1O/w1cDnyilFU=')
headers = {"Authorization":"Bearer p5M+z5sA0rK7XVnNsC1ctvNjuCqKhpqHpwt1b+h4KAI+JOPRRfTHT9IzcZRmrYykpNRRbPQ3oN6WxSW0zNS8Bja8uA9+fNSUgQ9/5yi065tPuM2brSTXgh/m80h6BUww5W/F1wZm5nfvwmukGZjP3QdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}

headers1 = {"Authorization":"Bearer p5M+z5sA0rK7XVnNsC1ctvNjuCqKhpqHpwt1b+h4KAI+JOPRRfTHT9IzcZRmrYykpNRRbPQ3oN6WxSW0zNS8Bja8uA9+fNSUgQ9/5yi065tPuM2brSTXgh/m80h6BUww5W/F1wZm5nfvwmukGZjP3QdB04t89/1O/w1cDnyilFU=","Content-Type":"image/jpeg"}

def get_richmenuid():
    body = {
    "size": {"width": 2500, "height": 843},
    "selected": "true",
    "name": "Controller",
    "chatBarText": "Controller",
    "areas":[
        {
          "bounds": {"x": 551, "y": 325, "width": 321, "height": 321},
          "action": {"type": "message", "text": "up"}
        },
        {
          "bounds": {"x": 876, "y": 651, "width": 321, "height": 321},
          "action": {"type": "message", "text": "right"}
        },
        {
          "bounds": {"x": 551, "y": 972, "width": 321, "height": 321},
          "action": {"type": "message", "text": "down"}
        },
        {
          "bounds": {"x": 225, "y": 651, "width": 321, "height": 321},
          "action": {"type": "message", "text": "left"}
        },
        {
          "bounds": {"x": 1433, "y": 657, "width": 367, "height": 367},
          "action": {"type": "message", "text": "btn b"}
        },
        {
          "bounds": {"x": 1907, "y": 657, "width": 367, "height": 367},
          "action": {"type": "message", "text": "btn a"}
        }
    ]
    }
    req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu', headers=headers,data=json.dumps(body).encode('utf-8'))
    dict_req = json.loads(req.text)
    #print(dict_req)
    print(dict_req['richMenuId'])
    return dict_req['richMenuId']

# def upload_img():
#     with open(r"F:/Line-login-starter/uplodimg/richimg.jpg", 'rb') as f:
#         line_bot_api.set_rich_menu_image(get_richmenuid(), "image/jpeg", f)

def start_upload():
    body = {
        "size": {"width": 2500, "height": 843},
        "selected": "true",
        "name": "Controller",
        "chatBarText": "Controller",
        "areas": [
            {
                "bounds": {"x": 551, "y": 325, "width": 321, "height": 321},
                "action": {"type": "message", "text": "up"}
            },
            {
                "bounds": {"x": 876, "y": 651, "width": 321, "height": 321},
                "action": {"type": "message", "text": "right"}
            },
            {
                "bounds": {"x": 551, "y": 972, "width": 321, "height": 321},
                "action": {"type": "message", "text": "down"}
            },
            {
                "bounds": {"x": 225, "y": 651, "width": 321, "height": 321},
                "action": {"type": "message", "text": "left"}
            },
            {
                "bounds": {"x": 1433, "y": 657, "width": 367, "height": 367},
                "action": {"type": "message", "text": "btn b"}
            },
            {
                "bounds": {"x": 1907, "y": 657, "width": 367, "height": 367},
                "action": {"type": "message", "text": "btn a"}
            }
        ]
    }
    req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu/richmenu-697712a1598fe4513baa5d7d669d4f6f/content',headers=headers1,data=json.dumps(body).encode('utf-8'))
    print(req.text,"-------")
if __name__ == '__main__':
    #upload_img()
    start_upload()

