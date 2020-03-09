#coding:utf-8
import requests

url = "http://106.ihuyi.com/webservice/sms.php?method=Submit"

#APIID
account = "C55576940"
#APIkey
password = "dd3662684b749bdd15836208b40b85f8"

mobile = "15266356525"
content = "您的验证码是：153859。请不要把验证码泄露给其他人。"
#请求头
headers = {
    "Content-type": "application/x-www-form-urlencoded",
    "Accept": "text/plain"
}
#请求数据
data = {
    "account": account,
    "password": password,
    "mobile": mobile,
    "content": content,
}
#��������
response = requests.post(url,headers = headers,data=data)
    #url 请求地址
    #headers 请求头
    #data 请求数据

print(response.content.decode())