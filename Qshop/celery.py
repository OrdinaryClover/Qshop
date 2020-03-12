##管理控制celery
import os
from celery import Celery
from django.conf import settings

##设置celery环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE','CeleryTask.settings')

##实例化
app = Celery("Qshop_celery")   ##参数为celery应用的名字，可以随便

##加载celery 设置
app.config_from_object('django.conf:settings')


##如果项目中，创建了task.py namecelery就会沿着app去寻找task.py文件，来完成任务
app.autodiscover_tasks(lambda :settings.INSTALLED_APPS)