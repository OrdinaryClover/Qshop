from django.urls import path,re_path
from .views import *

urlpatterns = [
    path("alipay_order/",alipay_order),
    path("pay_aliresult/",pay_aliresult),
    path("cart/",cart),
    path("add_cart/",add_cart),
    path("change_cart/",change_cart),
    path("cart_place_order/",cart_place_order),
    path("user_center_order/",user_center_order),
    path("get_cachegoods/",get_cachegoods),
    path("update_cachegoods/",update_cachegoods),

]
