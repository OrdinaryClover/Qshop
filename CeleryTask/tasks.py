##用于编写任务

##1、导包
from __future__ import absolute_import
from Qshop.celery import app

@app.task
def TaskTest():
    print("hello")

@app.task
def Myprint(num):
    print(num)

from sdk.send163 import sendQQ_Email
@app.task
def send_yibu_163(param):
    sendQQ_Email(param)