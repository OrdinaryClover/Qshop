from django.db import models
from Seller.models import *
# Create your models here.

ORDER_STATUS = (
    (1,"未支付"),
    (2,"已支付"),
    (3,"待发货"),
    (4,"已发货"),
    (5,"拒收"),
    (6,"已完成"),
)


class PayOrder(models.Model):
    order_number = models.CharField(max_length=36,unique=True,verbose_name="订单编号")
    order_date = models.DateField(auto_now=True,verbose_name="订单创建时间")
    order_status = models.IntegerField(choices=ORDER_STATUS,verbose_name="订单状态")
    order_total = models.FloatField(verbose_name="订单总价")
    order_user = models.ForeignKey(to = LoginUser,on_delete=models.CASCADE)

    class Meta:
        db_table = "payorder"

class OrderInfo(models.Model):
    order = models.ForeignKey(to=PayOrder,on_delete=models.CASCADE)
    goods = models.ForeignKey(to=Goods,on_delete=models.CASCADE)
    goods_price = models.FloatField(verbose_name="商品的单价")
    store = models.ForeignKey(to=LoginUser,on_delete=models.CASCADE,verbose_name="卖家")
    goods_count = models.IntegerField(verbose_name="购买的单品的数量")
    goods_total_price = models.FloatField(verbose_name="购买的单品总金额")

    class Meta:
        db_table = "orderinfo"
class Cart(models.Model):
    goods = models.ForeignKey(to=Goods,on_delete=models.CASCADE)
    goods_number = models.IntegerField(verbose_name="商品的数量")
    goods_total = models.FloatField(verbose_name="商品的小计")
    # goods_price = models.FloatField(verbose_name="商品的价格")
    cart_user = models.ForeignKey(to=LoginUser,on_delete=models.CASCADE,verbose_name="买家")

    class Meta:
        db_table = "cart"


class PayorderAddress(models.Model):
    name = models.CharField(max_length=32,verbose_name="收货人姓名")
    phone = models.CharField(max_length=11,verbose_name="联系电话")
    address = models.TextField(verbose_name="收货人地址")
    payorder = models.OneToOneField(to=PayOrder,on_delete=models.CASCADE)  ##一对一

