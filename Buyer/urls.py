from django.urls import path,re_path
from .views import *

urlpatterns = [
    path("alipay_order/",alipay_order),
    path("pay_aliresult/",pay_aliresult),
    path("cart/",cart),
    path("add_cart/",add_cart),

]
