from django.urls import path,re_path
from .views import *
urlpatterns = [
    path('login/', login),
    path('logout/', logout),
    path('register/', register),
    path('index/', index),
    re_path('goodslist/(?P<page>\d+)/(?P<status>\d+)/', goods_list),
    re_path('goods_list_api/(?P<page>\d+)/(?P<status>\d+)/', goods_list_api),
    re_path('goodsstatus/(?P<id>\d+)/(?P<status>\w+)/', goods_status),
    path('user_profile/',user_profile),
    path('goods_add/',goods_add),
    path('get_code/',get_code),
    # path('add_label/',add_label),

]