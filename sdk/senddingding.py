import requests
import json

data = {
        "msgtype": "text",
        "text": {
            "content": "我就是我, 是不一样的烟火2121验证码"
        },
        "at": {
            "atMobiles": [
                # "156xxxx8827",
                # "189xxxx8325"
            ],
            "isAtAll": True
        }
}

# 发送请求
url = ""
headers = {'Content-Type': 'application/json'}
##转json
data = json.dumps(data)

resp = requests.post(url,headers = headers,data = data)

print(resp.content.decode())

