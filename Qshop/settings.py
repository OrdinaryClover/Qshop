"""
Django settings for Qshop project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#=$jr==4lfat15y+cl!ec8j--(8^kye19x&!(o31q6-%e^_rz3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Buyer',
    'Buyer.templates',
    'Seller',
    'djcelery',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'Qshop.middleware01.MiddleWareTest'
]

ROOT_URLCONF = 'Qshop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Qshop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     ##一主   配置权重
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     },
#     'master': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     },
#     ##多从   配置权重
#     'slave': {
#             'ENGINE': 'django.db.backends.sqlite3',
#             'NAME': os.path.join(BASE_DIR, 'dbslave.sqlite3'),
#     },
#     'slave1': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'dbslave.sqlite3'),
#     }
# }
#
#
# DATABASE_ROUTERS = ["Qshop.mydbrouter.Router"]


DATABASES = {
    'default':{
        'ENGINE':'django.db.backends.mysql',
        'NAME':'qshop',
        'HOST':'127.0.0.1',
        'USER':'root',
        'PAWWEORD':"",
        'PORT':3306,
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

# USE_TZ = True
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'static'),
)
#
# STATIC_ROOT = os.path.join(BASE_DIR,"static")

#媒体文件配置
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,"static")


##支付宝支付demo
from alipay import AliPay
app_public_key_string ="""-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAnU3NoYc29srk32gPmDsT4RAC7h2p9mMYMvxnS3mk2Gl718ZHVwYySL6AdXS9PN800/3KpgwZne+8PBVFFWkOrS//cSR/dFVnHXXQq/Tc4z4YxviMRubKBsxCTNJh+RZFK1u9OuunjNXKZJ/yYd7pt6xcT5TrSrvWiBNhHCUI1coxjno3sItMtTPPlwlYJh2tXOwd4MliMPNjTEUklIR24430EBC16kpNsXTqY227nAraEXyiG+m3AFu+GSFZmdqI7/zDcsQ62FgUTAZDn3I+CU4eiS1IeKr3U2muwqLVQPSzXxh72iMtiDvVnjoD4HacqYpnDOTtQABj9zQOWRwrkQIDAQAB
-----END PUBLIC KEY-----"""
app_private_key_string ="""-----BEGIN PRIVATE KEY-----
MIIEpAIBAAKCAQEAnU3NoYc29srk32gPmDsT4RAC7h2p9mMYMvxnS3mk2Gl718ZHVwYySL6AdXS9PN800/3KpgwZne+8PBVFFWkOrS//cSR/dFVnHXXQq/Tc4z4YxviMRubKBsxCTNJh+RZFK1u9OuunjNXKZJ/yYd7pt6xcT5TrSrvWiBNhHCUI1coxjno3sItMtTPPlwlYJh2tXOwd4MliMPNjTEUklIR24430EBC16kpNsXTqY227nAraEXyiG+m3AFu+GSFZmdqI7/zDcsQ62FgUTAZDn3I+CU4eiS1IeKr3U2muwqLVQPSzXxh72iMtiDvVnjoD4HacqYpnDOTtQABj9zQOWRwrkQIDAQABAoIBAQCHPuysk4/rUnjDqDm4PhsSZ2zNg82s3Hhi5eZ92wGjW9Yxp/WQWfCD4N6bnhpSKurF1bAVYdPomcVytyrlhKUsvFbY1XOL9x2oE7KtFeOQscQl1m7tSuKqQ5ZBbKT1v3MLG14wOYqeKPZR279O7JRv6g6YEcbXQ3bpGhhlVWYqQMmB7cke+JqNslwkNDo4x2OVXYWiBkubiuYT1RLSKLj/TNPbxdRFo2ZpOYbzOLlSuu556VOz+NOcPq+t5u+hYSf+612ko3BXN7N01O6psWKoHowMt3gaRbFFQudnOJXGU5aqCKtJtnzzrzfLrSABRz1kRfopE5jUcCU+VtMK6hwBAoGBAN/yPd9Rr+nLfi/QqngXhSDDiW3OtNgdlP0QitUEihKqOskdFpog826t+AilxMF1u1B6svFXjaRG0pmzaLcJAxEmNfcKhRmBF1+VdurK0/Jf4yqpJ/ag86Fmbm1RXbsZg13VCyGLj1LkEOMqCM//Huh5HLQmzij0TnhgSz0LRYNRAoGBALPRrUzG9n5k0tVliJXJvWFB5lH0RH/2iz0ZhnpmYJwmzFYTYrZ10AyX7joG5i+tLTwaqXGuqcGIElvKdN12oMBk2b70XYwtcytoiVfUA4zKumjDZ6VnXKLAsoYau/RMxe4TssNODAjKhXXp/+1/nsH2SVnDlXcut9UgFZODG5RBAoGAahqxG/ztFx2WJPt9uTaTmelrVL6KSpcBf0F2NeVXse47ugvxKIeSLw94JEi+R1cLr97ip5xu/LWdlLs/UvGPJXHwQaMXWvUh6OS9GhONhhnOXOkWiTDLHd6VVXAms74r0qpdAsDH4GM0aR0CXeInd8fiRKzaIudVwo0FON/9SHECgYEAqh6qp8JsHTPhywXd7GgKBONFtS81RyLGpC1r7ozAxbpnAuAgOaLIC8IJHVi9mUlrTDulJuopq/DB/ZlSatr6RkqjPmcNwbqWBPFHTpJEMYTySn7jpbZeC5Pm0bylKQEhGJYGP4OtGvwOu3mAKP7eAX6x8nx5AWJvhPBvuTkGdIECgYA/Py2NyOIgg9pHkWPIcz3+jFYHjDjpMFZr7vCw0rSNC1AjDid0nR/7CKDN/yQLllXGjrLKk1yLGNuV0T1AoE7QNsKN6onp5cfS28wWgefZW83cbzXxZDry9I5sSMyRUZZLuoo+DToER6uthEZKYiQ9l5MrLZmtaLXW+RrfWuGXmA==
-----END PRIVATE KEY-----"""


##创建实例对象
alipay =AliPay(
    appid = "2016101900723700",
    app_notify_url = None,
    app_private_key_string=app_private_key_string,
    alipay_public_key_string=app_public_key_string,
    sign_type="RSA2",
    debug=False
)


##celery设置
import djcelery
djcelery.setup_loader()
BROKER_URL = "redis://127.0.0.1:6379/1"  ##指定broker的存储位置，消息中间价   redis中间人

CELERY_IMPORTS = ("CeleryTask.tasks")  ##指定任务文件

CELERY_TIME_ZONE = "Asia/Shanghai" ##时区

CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"##驱动

from celery.schedules import timedelta,crontab
CELERYBEAT_SCHEDULE = {
    u"测试01":{
        "task":"CeleryTask.tasks.Test",        ##定时任务要执行的任务
        # "schedule":timedelta(seconds=2)          ##每两秒执行一次
        # "schedule":crontab(hour=2),          ##每小时执行一次
        "schedule":crontab(minute=2),         ##每小时执行一次
    }
}


# #缓存
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION':[
#             "127.0.0.0:11211"   ##使用本地的memcache缓存
#         ]
#     }
# }
#
# #Django日志配置
#
# LOGGING = {
#     'version':1,
#     'disable_exsiting_loggers':True,
#     'handlers':{
#         ###放置句柄的地方
#         'file':{
#             'level':'WARNING',                            ###代表要收集到文件中的日志等级
#             'class':'logging.FileHandler',
#             'filename':os.path.join(BASE_DIR,'django.log'),     ####日志收集在 django.log中
#             'encoding':'utf-8',     ####编码
#         }
#     },
#     'loggers':{
#         ####收集日志
#         'django':{
#             ####收集日志的人员之一
#             'handlers':['file'],
#             'level':'DEBUG',   ###django这个收集器收集的日志等级
#
#         }
#     }
# }