from django.shortcuts import render
import hashlib
from django.http import HttpResponseRedirect
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
    order_num = str(uuid.uuid4())
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


