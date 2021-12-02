
# 載入需要的模組
from __future__ import unicode_literals
import os
import configparser
import urllib
import requests
import json
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, StickerMessage,ImageSendMessage, FlexSendMessage

import re
import random
app = Flask(__name__)

# LINE 聊天機器人的基本資料
config = configparser.ConfigParser()
config.read('config.ini')
line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))

# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    
    try:
        print(body)
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

startmenu = FlexSendMessage(
                    alt_text='menu',
                    contents={
                "type": "bubble",
                "size": "kilo",
                "hero": {
                    "type": "image",
                    "url": "https://miro.medium.com/max/700/1*a9sc8WdCtcphPb1REjAnbA.jpeg",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover",
                    "action": {
                    "type": "postback",
                    "label": "action",
                    "data": "hello"
                    }
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents":  [
                    {
                        "type": "text",
                        "text": "功能選單",
                        "weight": "bold",
                        "size": "xl",
                        "margin": "none",
                        "align": "center"
                    },
                    {
                        "type": "text",
                        "text": "(有時候連線到表單以及送出表單後要等一下，網頁會重新整理喔!)",
                        "weight": "bold",
                        "size": "xs",
                        "margin": "sm",
                        "align": "start",
                        "contents": [
                        {
                            "type": "span",
                            "text": "(有時候連線到表單以及送出表單後要"
                        }
                        ]
                    },
                    {
                        "type": "text",
                        "contents": [
                        {
                            "type": "span",
                            "text": "等一下，網頁會重新整理喔!)",
                            "size": "xs"
                        }
                        ],
                        "margin": "none",
                        "size": "xs",
                        "weight": "bold"
                    }
                    ],
                    "margin": "xs",
                    "spacing": "xs"
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "none",
                    "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "message",
                        "label": "關於這個app",
                        "text": "了解詳情"
                        }
                    },
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "message",
                        "label": "開發時問題及困難",
                        "text": "開發問題"
                        }
                    },
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "uri",
                        "label": "送食物的表單",
                        "uri": "https://liff.line.me/1656540074-QGvA1Pdz"
                        }
                    },
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                        "type": "message",
                        "label": "我想看看有沒有食物",
                        "text": "我想訂餐"
                        }
                    },
                    {
                        "type": "spacer",
                        "size": "sm"
                    }
                    ],
                    "flex": 0
                }
                }
                )

@handler.add(MessageEvent, message=StickerMessage)
def start(event):
    line_bot_api.reply_message(
                    event.reply_token,
                    startmenu
                )

# 幫你query目前所有可用訂單
@handler.add(MessageEvent, message=TextMessage)
def getAll(event):
    if event.message.text == "我想訂餐":
        try: 
            contents=[]
            r = requests.get('https://a6be-140-113-124-40.ngrok.io/getAll')
            data = json.loads(r.text)
            
            if(len(json.loads(r.text))!=0):
                for i in range(len(data)):
                    print(str(data[i]['name']))
                    contents.append({
                        "type": "bubble",
                        "hero": {
                            "type": "image",
                            "url": str(data[i]['name']),
                            "size": "full",
                            "aspectRatio": "20:13",
                            "aspectMode": "cover",
                            "action": {
                            "type": "uri",
                            "uri": "https://3778-140-113-124-40.ngrok.io/detail/"+str(data[i]['id'])
                            }
                        },
                        "body": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "text",
                                "text": data[i]['item'],
                                "weight": "bold",
                                "size": "xl"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "margin": "lg",
                                "spacing": "sm",
                                "contents": [
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "spacing": "sm",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": "地點",
                                        "color": "#aaaaaa",
                                        "size": "sm",
                                        "flex": 3
                                    },
                                    {
                                        "type": "text",
                                        "text": data[i]['location'],
                                        "wrap": True,
                                        "color": "#666666",
                                        "size": "sm",
                                        "flex": 5
                                    }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "spacing": "sm",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": "最晚領取時間",
                                        "color": "#aaaaaa",
                                        "size": "sm",
                                        "flex": 3,
                                        "margin": "none"
                                    },
                                    {
                                        "type": "text",
                                        "text": data[i]['time'][0:5],
                                        "wrap": True,
                                        "color": "#666666",
                                        "size": "sm",
                                        "flex": 5
                                    }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": "還有",
                                        "flex": 3,
                                        "margin": "none",
                                        "size": "sm",
                                        "color": "#aaaaaa"
                                    },
                                    {
                                        "type": "text",
                                        "text": str(data[i]['left']) + '份',
                                        "flex": 5,
                                        "size": "sm",
                                        "color": "#666666"
                                    }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": "一人最多可拿",
                                        "flex": 3,
                                        "margin": "none",
                                        "size": "sm",
                                        "color": "#aaaaaa"
                                    },
                                    {
                                        "type": "text",
                                        "text": str(data[i]['max']) + '份',
                                        "flex": 5,
                                        "size": "sm",
                                        "color": "#666666"
                                    }
                                    ]
                                }
                                ]
                            }
                            ]
                        },
                        "footer": {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "button",
                                "style": "link",
                                "height": "sm",
                                "action": {
                                "type": "uri",
                                "label": "我想預約",
                                "uri": "https://3778-140-113-124-40.ngrok.io/detail/"+str(data[i]['id'])
                                #"uri": "https://liff.line.me/1656540074-b62ev3dG?id="+str(data[i]['id'])
                                }
                            },
                            {
                                "type": "button",
                                "style": "link",
                                "height": "sm",
                                "action": {
                                "type": "uri",
                                "label": "我想預約(liff版 尚未完成)",
                                #"uri": "https://3778-140-113-124-40.ngrok.io/detail/"+str(data[i]['id'])
                                "uri": "https://liff.line.me/1656540074-b62ev3dG?id="+str(data[i]['id'])
                                }
                            },
                            {
                                "type": "button",
                                "style": "link",
                                "height": "sm",
                                "action": {
                                "type": "message",
                                "label": "功能選單",
                                "text": "呼叫功能選單"
                                }
                            },
                            ],
                            "flex": 0
                        }
                    })
                print(contents)
                flex_message = FlexSendMessage(
                    alt_text='hello',
                    contents={
                        "type": "carousel",
                        "contents":contents
                    }
                )
            
                #測試flex版
                line_bot_api.reply_message(
                    event.reply_token,
                    flex_message
                )
                
            else:
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text='很抱歉,目前可能沒有沒有人贈送免費的食物喔~ 請在稍等看看! 或是你有吃不完的食物可以送給大家的話 趕快一起填表單吧!')
                )
            
            
        # getall不到   
        except:
            line_bot_api.reply_message(
                event.reply_token,
                 TextSendMessage(text='很抱歉,目前可能沒有沒有人贈送免費的食物喔~ 請在稍等看看! 或是直接點選右下角的圖示也可以自己送出愛心食物喔!')
            )
    elif(event.message.text == "呼叫功能選單"):
        line_bot_api.reply_message(
                    event.reply_token,
                    startmenu
                )
    

if __name__ == "__main__":
    app.run()

