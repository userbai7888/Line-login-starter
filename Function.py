#這個檔案的作用是：建立功能列表

#===============import=============
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
#===============LINEAPI=============================================

#以下是本檔案的內容本文

#1.建立旋轉木馬訊息，名為function_list(未來可以叫出此函數來使用)
#function_list的括號內是設定此函數呼叫時需要給函數的參數有哪些

def function_list():
    message = TemplateSendMessage(
        alt_text='功能列表',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQkl5qgGtBxZbBu921rynn7HN7C7JaD_Hbi5cMMV5gEgQu2mE-rIw',
                    title='Dawn商城',
                    text='百萬種商品一站購買',
                    actions=[
                        MessageTemplateAction(
                            label='關於Dawn商城',
                            text='Dawn商城是什麼呢?'
                        ),
                        URITemplateAction(
                            label='點我逛商場',
                            uri='http://th.fashionlian.com/m/index.html'
                        )
                    ]
                ),

                CarouselColumn(
                    thumbnail_image_url='https://img.shop.com/Image/Images/11module/MABrands/opc3Chews_usa_32979_LogoTreatment_200x75.svg',
                    title='獨家商品',
                    text='百種優質獨家商品',
                    actions=[
                        MessageTemplateAction(
                            label='點我看產品目錄',
                            text='獨家商品有哪些？'
                        ),
                        URITemplateAction(
                            label='購買獨家品牌',
                            uri='http://th.fashionlian.com/m/index.html'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://img.shop.com/Image/featuredhotdeal/GOMAJI1551245496503.jpg',
                    title='優惠資訊',
                    text='隨時更新最新優惠',
                    actions=[
                        MessageTemplateAction(
                            label='抽一個優惠',
                            text='抽優惠資訊'
                        ),
                        URITemplateAction(
                            label='近期優惠資訊',
                            uri='http://th.fashionlina.com/m/product_561023562565197.html'
                        )
                    ]
                ),
                # CarouselColumn(
                #     thumbnail_image_url='https://img.shop.com/Image/featuredhotdeal/Carrefour1551245288925.jpg',
                #     title='最新消息',
                #     text='最新活動訊息',
                #     actions=[
                #         MessageTemplateAction(
                #             label='點我看最新消息',
                #             text='我想瞭解最新活動'
                #         ),
                #         URITemplateAction(
                #             label='活動資訊頁面',
                #             uri='http://th.fashionlina.com/m/product_561023562565197.html'
                #         )
                #     ]
                # ),
                # CarouselColumn(
                #     thumbnail_image_url='http://img.technews.tw/wp-content/uploads/2014/05/TechNews-624x482.jpg',
                #     title='每日新知',
                #     text='定期更新相關資訊',
                #     actions=[
                #         MessageTemplateAction(
                #             label='點我看每日新知',
                #             text='抽一則每日新知'
                #         ),
                #         URITemplateAction(
                #             label='更多更新內容',
                #             uri='https://www.youtube.com/channel/UCpzVAEwEs9AwT2uAOZuxaRQ?view_as=subscriber'
                #         )
                #     ]
                # ),
                #
                # CarouselColumn(
                #     thumbnail_image_url='https://img.shop.com/Image/Images/landingPages/ps-recruit/twn-ps-recruit-header.jpg',
                #     title='招商說明',
                #     text='與Shop.com合作',
                #     actions=[
                #         MessageTemplateAction(
                #             label='招商資訊',
                #             text='如何成為夥伴商店'
                #         ),
                #         URITemplateAction(
                #             label='招商說明報名頁面',
                #             uri='https://www.taobao.com'
                #         )
                #     ]
                # ),
                # CarouselColumn(
                #     thumbnail_image_url='https://images.marketamerica.com/site/br/images/logos/awards/torch-award-ethics-2018.jpg',
                #     title='微型創業資訊',
                #     text='加入網路微型創業趨勢',
                #     actions=[
                #         MessageTemplateAction(
                #             label='瞭解更多',
                #             text='什麼是微型創業資訊'
                #         ),
                #         URITemplateAction(
                #             label='公司簡介',
                #             uri='https://www.marketamerica.com/?localeCode=zh-Hant&redirect=true'
                #         )
                #     ]
                # ),
                # CarouselColumn(
                #     thumbnail_image_url='https://scontent-sjc3-1.xx.fbcdn.net/v/t1.0-1/p320x320/50934385_2553136691368417_7766092240367124480_n.jpg?_nc_cat=109&_nc_ht=scontent-sjc3-1.xx&oh=c144a6b45450781ccaf258beb40bc53e&oe=5D228BF1',
                #     title='聯繫White本人',
                #     text='直接聯繫White',
                #     actions=[
                #         MessageTemplateAction(
                #             label='誰是White?',
                #             text='White是誰？想認識'
                #         ),
                #         URITemplateAction(
                #             label='加我的LINE',
                #             uri='https://line.me/ti/p/KeRocPY6PP'
                #         )
                #     ]
                #)
            ]
        )
    )
    return message