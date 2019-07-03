from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

def women_test():
    message = TemplateSendMessage(
        alt_text='图片轮播图',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/Ktiux3g.jpg",
                    action=URITemplateAction(
                        label="连衣裙",
                        uri="https://i.imgur.com/Ktiux3g.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/e4BWXnb.jpg",
                    action=URITemplateAction(
                        label="碎花衣",
                        uri="https://i.imgur.com/e4BWXnb.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/nRCvBau.jpg",
                    action=URITemplateAction(
                        label="漂亮姐姐",
                        uri="https://i.imgur.com/nRCvBau.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/9qMNCoS.jpg",
                    action=URITemplateAction(
                        label="漂亮衣服",
                        uri="https://i.imgur.com/9qMNCoS.jpg"
                    )
                )
            ]
        )
    )
    return message



def men_test():
    message = TemplateSendMessage(
        alt_text='图片轮播图',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/uKYgfVs.jpg",
                    action=URITemplateAction(
                        label="新鮮水果",
                        uri="https://www.youtube.com/watch?v=1baqfP7g_Cg&feature=youtu.be"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/QOcAvjt.jpg",
                    action=URITemplateAction(
                        label="新鮮蔬菜",
                        uri="https://cdn.101mediaimage.com/img/file/1410464751urhp5.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/Np7eFyj.jpg",
                    action=URITemplateAction(
                        label="可愛狗狗",
                        uri="http://imgm.cnmo-img.com.cn/appimg/screenpic/big/674/673928.JPG"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/QRIa5Dz.jpg",
                    action=URITemplateAction(
                        label="可愛貓咪",
                        uri="https://m-miya.net/wp-content/uploads/2014/07/0-065-1.min_.jpg"
                    )
                )
            ]
        )
    )
    return message