from django.shortcuts import render
import hashlib
from django.http import HttpResponseRedirect,JsonResponse
from Seller.models import *
from .models import *
# Create your views here.
#加密
def setPassword(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    result = md5.hexdigest()
    return result
##校验登录
def loginValid(func):
    def inner(request,*args,**kwargs):
        ##校验登录
        cookie_email = request.COOKIES.get("buy_email")
        session_email = request.session.get("buy_email")
        if cookie_email and session_email and cookie_email == session_email:
            flag = LoginUser.objects.filter(email=cookie_email,id=request.COOKIES.get("buy_userid"),user_type=1).exists()
            if flag:
                return func(request,*args,**kwargs)
            else:
                return HttpResponseRedirect("/login/")
        else:
            return HttpResponseRedirect("/login/")
    return inner
##注册
def register(request):
    print(request.POST)
    username = request.POST.get("username")
    email = request.POST.get("email")
    password = request.POST.get("pwd")
    repassword = request.POST.get("cpwd")
    if username and email and password and repassword:
        LoginUser.objects.create(username=username,email=email,password=setPassword(password),user_type=1)
        return HttpResponseRedirect("/login/")
    else:
        message = "请输入账号密码"
    return  render(request,"buyer/register.html",locals())

##登录
def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username and password:
            user = LoginUser.objects.filter(username=username,password=setPassword(password),user_type=1).first()
            if user:
                response = HttpResponseRedirect("/index/")
                response.set_cookie("buy_email",user.email)
                response.set_cookie("buy_username",user.username)
                response.set_cookie("buy_userid",user.id)
                request.session["buy_email"] = user.email
                return response
            else:
                message = "账号密码不正确"
        else:
            message = "账号密码不能为空"

    return render(request,"buyer/login.html",locals())

def logout(request):
    resp = HttpResponseRedirect("/login/")
    resp.delete_cookie("buy_email")
    resp.delete_cookie("buy_username")
    resp.delete_cookie("buy_userid")
    del request.session["buy_email"]
    return resp



#首页
@loginValid
def index(request):
    """
    1、如果类型下面没有商品，类型不展示
    2、如果类型下面超过四个商品，只展示四个
    3、如果类型下面商品数量大于0.小于4应该展示商品
    :param request:
    :return:
    """
    goods_type = GoodsType.objects.all()
    ##处理返回的数据，构建数据
    # res = [{"type":"新鲜水果.obj","goods":"goods1,goods2,goods3"},{},{}]
    res = []
    for one in goods_type:
        goods = one.goods_set.order_by("id").all()
        if len(goods) > 4:
            goods_list = goods[:4]
            res.append({"type":one,"goods_list":goods_list})
        elif len(goods) > 0 and len(goods) < 4:
            goods_list = goods
            res.append({"type": one, "goods_list": goods_list})
        print(res)
    return render(request,"buyer/index.html",locals())

def base(request):
    return render(request,"buyer/base.html")


##商品列表
def goods_list(request):
    req_type = request.GET.get("req_type")
    kywards = request.GET.get("kywards")
    ##查看更多
        ##kywards 应该为类型的id
    if req_type == "find_all":
        good_type = GoodsType.objects.filter(id=kywards).first()
        goods = good_type.goods_set.order_by("-goods_pro_time")
    ##搜索
        ##kyward应该为商品的名字
        ##模糊查询
    else:
        goods = Goods.objects.filter(goods_name__contains=kywards).all()
        print(goods)

    goods_new =goods[:2]
    return render(request,"buyer/goods_list.html",locals())


def goods_detail(request):
    ##通过商品的id获取商品
    goods_id = request.GET.get("goods_id")
    goods = Goods.objects.get(id=goods_id)
    return render(request, "buyer/goods_detail.html", locals())



##生成订单号
def get_order_no():
    import uuid
    order_num = str(uuid.uuid4()).replace("-","")
    return order_num
@loginValid
def place_order(request):
    ##保存数据
    ##获取买家的user_id
    user_id = request.COOKIES.get("buy_userid")
    goods_id = request.GET.get("goods_id")
    goods_count = int(request.GET.get("goods_count"))

    ##查找商品
    goods = Goods.objects.get(id=goods_id)

    ##payorder
    payorder = PayOrder()
    payorder.order_number = get_order_no()
    payorder.order_status = 1  ##未支付
    payorder.order_total = goods_count * goods.goods_price
    payorder.order_user_id = int(user_id)
    payorder.save()

    ##orderinfo
    order_info = OrderInofo()
    order_info.order = payorder
    order_info.goods = goods
    order_info.goods_price = goods.goods_price
    ##店铺的信息 通过商品寻找店铺
    order_info.store = goods.goods_store
    order_info.goods_count = goods_count
    order_info.goods_total_price = goods_count * goods.goods_price
    order_info.save()

    yunfei = 10
    add_yunfei = yunfei + int(payorder.order_total)

    return render(request,"buyer/place_order.html",locals())

def gettest(request):
    from django.http import HttpResponse

from Qshop.settings import alipay
def alipay_order(request):
    payorder_id = request.GET.get("payorder_id")
    payorder = PayOrder.objects.get(id = payorder_id)
    ##实例一个订单
    order_string = alipay.api_alipay_trade_page_pay(
        subject="每日生鲜",  ##主题
        out_trade_no=payorder.order_number,  ##订单号
        total_amount= str(int(payorder.order_total) + 10),  ##交易金额  字符串
        return_url= "http://127.0.0.1:8000/buyer/pay_aliresult/",  ##回调的地址
        notify_url=None,  ##通知
    )
    ##返回支付宝支付的url
    result = "https://openapi.alipaydev.com/gateway.do?" + order_string
    return HttpResponseRedirect(result)


##接收是否支付成功的结果
def pay_aliresult(request):
    out_trade_no = request.GET.get("out_trade_no")

    payorder = PayOrder.objects.get(order_number=out_trade_no)
    payorder.order_status = 2
    payorder.save()

    return render(request,"buyer/pay_result.html",locals())

from django.db.models import Sum
@loginValid
def cart(request):
    ##查看登录用户的购物车内容
    user_id = request.COOKIES.get("buy_userid")
    # cart = Cart.objects.filter(cart_user_id=int(user_id)).all()
    cart = Cart.objects.filter(cart_user=LoginUser.objects.get(id=int(user_id))).all()

    ##获取商品的数量之和
    ##聚合
    ##all_total 字典  key:value
    all_total = cart.aggregate(sum_total = Sum("goods_total"),sum_number = Sum("goods_number"))


    return render(request,"buyer/cart.html",locals())

@loginValid
def add_cart(request):
    result = {"code":10000,"msg":"添加购物车成功"}
    user_id = request.COOKIES.get("buy_userid")
    data = request.POST
    print(data)
    goods_id = data.get("goods_id")
    goods_count = data.get("goods_count",1)   ##商品详情页   指定默认值1
    goods = Goods.objects.get(id=goods_id)
    ##判断购物车中是否已经存在该商品

    cart = Cart.objects.filter(goods=goods).first()
    if cart:
        cart.goods_number += goods_count
        cart.goods_total += goods.goods_price * goods.goods_count
    else:
        ##添加购物车
        cart = Cart()
        cart.goods = goods
        cart.goods_number = goods_count
        cart.goods_total = int(goods_count) * goods.goods_price
        cart.cart_user_id = user_id
    try:
        cart.save()
        result = {"code":10000,"msg":"添加购物车成功"}
    except:
        result = {"code": 10001,"msg": "添加购物车失败"}

    return JsonResponse(result)


def change_cart(request):
    result = {"code":10001,"msg":"操作失败"}
    ##修改购物车的数量，以及小计
    # 购物车的id   类型：/ 加法/减法
    ##并且存储的到数据库
    data = request.POST
    cart_id = request.POST.get("cart_id")
    js_type = request.POST.get("js_type")
    print(cart_id)
    if cart_id and js_type:
        cart = Cart.objects.filter(id=int(cart_id)).first()
        if cart:
            if js_type == "add":
                cart.goods_number += 1
                cart.goods_total += cart.goods.goods_price
            elif js_type == "reduce":
                if cart.goods_number > 1:
                    cart.goods_number -= 1
                    cart.goods_total -= cart.goods.goods_price
                else:
                    pass
            else:
                Cart.objects.filter(cart_id=int(cart_id)).delete()
            try:
                cart.save()
                result = {"code": 10000, "msg": "操作成功","data": {"goods_number": cart.goods_number, "goods_total": cart.goods_total}}
            except:
                result = {"code":10001,"msg":"操作失败"}
        else:
            result = {"code": 10002, "msg": "商品不存在"}
    return JsonResponse(result)

##购物车去结算
@loginValid
def cart_place_order(request):
    print(request.POST)
    data = request.POST
    res = []
    for key,value in data.items():
        # print(key)
        # print(value)
        if key.startswith("cart_id"):
            res.append(value)
    print(res)
    #将购物车中选中的商品生成订单
    user_id = request.COOKIES.get("buy_userid")

    ##payorder
    payorder = PayOrder()
    payorder.order_number = get_order_no()
    payorder.order_status = 1  ##未支付
    payorder.order_total = 0   ##订单总价 = 订单详情中小计的和
    payorder.order_user_id = int(user_id)
    payorder.save()

    ##生成订单详情
    for one in res:
        cart = Cart.objects.filter(id = one).first()
        order_info = OrderInofo()
        order_info.order = payorder
        order_info.goods = cart.goods
        order_info.goods_price = cart.goods.goods_price
        ##店铺的信息 通过商品寻找店铺
        order_info.store = cart.goods.goods_store
        order_info.goods_count = cart.goods_number
        order_info.goods_total_price = cart.goods_total
        order_info.save()
        ##保存订单后从购物车中删除
        cart.delete()

    yunfei = 10
    payorder_total = payorder.orderinofo_set.aggregate(sum_total = Sum("goods_total_price")).get("sum_total")
    payorder.order_total = payorder_total
    payorder.save()

    add_yunfei = yunfei + payorder_total
    return render(request,"buyer/place_order.html",locals())


