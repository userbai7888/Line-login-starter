from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

# 女裝圖片展示
def women_test():
    message = TemplateSendMessage(
        alt_text='女式图片轮播图',
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


# 男裝圖片展示
def men_test():
    message = TemplateSendMessage(
        alt_text='男式图片轮播图',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/dXhB0Jx.jpg",
                    action=URITemplateAction(
                        label="男式襯衣",
                        uri="https://i.imgur.com/dXhB0Jx.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/ksFPg8Z.jpg",
                    action=URITemplateAction(
                        label="紅格子襯衫",
                        uri="https://i.imgur.com/ksFPg8Z.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/ubSzfrC.jpg",
                    action=URITemplateAction(
                        label="白格子襯衣",
                        uri="https://i.imgur.com/ubSzfrC.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/mVp88gI.jpg",
                    action=URITemplateAction(
                        label="西裝",
                        uri="https://i.imgur.com/mVp88gI.jpg"
                    )
                )
            ]
        )
    )

    return message