from django.shortcuts import render,HttpResponse
from django.http import  HttpResponseRedirect,JsonResponse
from .models import *
import hashlib,random
from django.core.paginator import Paginator
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
        cookie_email = request.COOKIES.get("seller_email")
        session_email = request.session.get("seller_email")
        if cookie_email and session_email and cookie_email == session_email:
            flag = LoginUser.objects.filter(email=cookie_email,id=request.COOKIES.get("seller_userid"),user_type=0).exists()
            if flag:
                return func(request,*args,**kwargs)
            else:
                return HttpResponseRedirect("/seller/login")
        else:
            return HttpResponseRedirect("/seller/login/")
    return inner

##注册
import datetime
def register(request):
    email = request.POST.get("email")
    password = request.POST.get("password")
    repassword = request.POST.get("repassword")
    code = request.POST.get("code")
    if email and password and repassword:
        if code:
            computer_code = ValidCode.objects.filter(user=email).order_by("-create_time").first()
            if code == computer_code.code:
                if int((datetime.datetime.now() -  computer_code.create_time).total_seconds())<300:
                    LoginUser.objects.create(email=email,password=setPassword(password),user_type=0)
                    return HttpResponseRedirect("/seller/login/")
                else:
                    message = "验证码失效，请重新获取"
            else:
                message = "验证码错误请重新输入"
        else:
            message = "请输入验证码"
    else:
        message = "请输入账号密码"
    return render(request,"seller/register.html",locals())



##登录
def login(request):
    print(request.POST)
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        if email and password:
            user = LoginUser.objects.filter(email=email,password=setPassword(password)).first()
            if user:
                response = HttpResponseRedirect("/seller/index")
                response.set_cookie("seller_email",user.email)
                response.set_cookie("seller_userid",user.id)
                request.session["seller_email"] = user.email
                return response
            else:
                message = "账号密码不正确"
        else:
            message = "账号密码不能为空"

    return render(request,"seller/login.html",locals())

from CeleryTask.tasks import TaskTest,Myprint
from django.views.decorators.cache import cache_page
##主页

@cache_page(60*5)   #代表生效五分钟
@loginValid
def index(request):
    print("helloword")
    # TaskTest.delay()  ##发布任务
    # Myprint.delay(10)      ##发布有参数的任务
    return render(request,"seller/index.html",locals())



##退出
def logout(request):
    response = HttpResponseRedirect("/seller/login/")
    response.delete_cookie("seller_email")
    del request.session["seller_email"]
    return response
##商品列表页面
@loginValid
def goods_list(request,status,page=1):
    ##根据状态 查询商品
    ##status 状态的标识
    ##0  下架的
    ##1 在售的
    # goods = Goods.objects.all()
    # goods = Goods.objects.filter(goods_status=status).order_by("id")
    goods = Goods.objects.filter(goods_status=status,goods_store_id=request.COOKIES.get("seller_userid")).order_by("id")
    ##分页情况供前端使用
    goods_obj = Paginator(goods,8)
    goods_list = goods_obj.page(page)
    return render(request,"seller/goods_list.html",locals())
##修改商品状态0/1
def goods_status(request,id,status):
    ##获取商品的id
    ##获取到是上架还是下架
    """
    :param request:
    :param id: 商品的id
    :param status:
            up  上架
            down 下架
    :return:
    """
    goods = Goods.objects.get(id=id)
    if status == "up":
        goods.goods_status = 1
        goods.save()
        # result = HttpResponseRedirect("/loginuser/goodslist/1/0/")
    elif status == "down":
        goods.goods_status = 0
        goods.save()
        # result = HttpResponseRedirect("/loginuser/goodslist/1/1/")
    url = request.META.get("HTTP_REFERER")
    return HttpResponseRedirect(url)

def goods_list_api(request,status,page=1):
    goods = Goods.objects.filter(goods_status=status).order_by("id")
    ##分页情况供前端使用
    goods_obj = Paginator(goods,8)
    goods_list = goods_obj.page(page)
    ##json
    result = {"code":10000,
              "msg":"成功",
              "date":""
              }
    res = []
    for one in goods_list:
        res_dict = {
            "goods_number":one.goods_number,
            "goods_name":one.goods_name,
            "goods_price":one.goods_price,
            "goods_count":one.goods_count,
            "goods_location":one.goods_location,
            "goods_safe_date":one.goods_safe_date,
            "goods_status":one.goods_status,
        }
        res.append(res_dict)

        result["date"] = res
        result["page"] = page
        result["page_range"] = list(goods_obj.page_range)
    # return JsonResponse(result)
##解决跨域请求
    response = JsonResponse(result)
    response["Access-Control-Allow-Origin"] = "*"  ##添加允许访问的主机 域名
    return response

##添加数据
# def goods_add(request):
#     goods_name = "萝卜、马铃薯、藕、甘薯、山药、芋头、茭白、苤蓝、慈姑、洋葱、生姜、大蒜、蒜薹、韭菜花、大葱、韭黄、冬瓜、南瓜、西葫芦、丝瓜、黄瓜、茄子、西红柿、苦瓜、辣椒、玉米、小瓜、菠菜、油菜、卷心菜、苋菜、韭菜、蒿菜、香菜、芥菜、芥兰"
#     goods_name = goods_name.split("、")
#     goods_address = "石家庄、沈阳、哈尔滨、杭州、福州、济南、广州、武汉、成都、昆明、兰州、台北、南宁、银川、太原、长春、南京、合肥、南昌、郑州、长沙、海口、贵阳、西安、西宁、呼和浩特、拉萨、乌鲁木齐"
#     goods_address = goods_address.split("、")
#     for i,j in enumerate(range(100),1):
#         goods = Goods()
#         goods.goods_number = str(i).zfill(5)
#         goods.goods_name = random.choice(goods_name) + random.choice(goods_address)
#         goods.goods_price = round(random.random()*100,2)   ##保留小数点两位
#         goods.goods_count = random.randint(1,100)
#         goods.goods_location = random.choice(goods_address)
#         goods.goods_safe_date = random.randint(1,32)
#         goods.save()
#     return HttpResponse("add goods")


##个人中心

@loginValid
def user_profile(request):
    ##返回用户的信息
    userid = request.COOKIES.get("seller_userid")
    user = LoginUser.objects.get(id=userid)
    ##处理post请求
    if request.method =="POST":
        data = request.POST
        # user.email = data.get("email")
        user.username = data.get("username")
        user.phone_number = data.get("phone_number")
        user.age= data.get("age")
        user.gender = data.get("gender")
        user.address = data.get("address")
        if request.FILES.get("img"):
            user.photo = request.FILES.get("img")
        user.save()
    return  render(request,"seller/user_profile.html",locals())


##添加商品
@loginValid
def goods_add(request):
    goods_type = GoodsType.objects.all()
    if request.method == "POST":
        userid = request.COOKIES.get("seller_userid")
        data = request.POST
        goods = Goods()

        goods.goods_number = data.get("goods_number")
        goods.goods_name = data.get("goods_name")
        goods.goods_price = data.get("goods_price")
        goods.goods_count = data.get("goods_count")
        goods.goods_location = data.get("goods_location")
        goods.goods_safe_date = data.get("goods_safe_date")
        goods.goods_picture = data.get("goods_picture")
        goods.goods_type_id = int(data.get("goods_type"))
        goods.goods_store = LoginUser.objects.get(id=userid)
        goods.goods_picture = request.FILES.get("img")
        goods.save()

    return render(request,"seller/goods_add.html",locals())


def add_label(request):
    GoodsType.objects.create(type_label="新鲜水果",type_description="新鲜水果",type_picture="img/banner01.jpg")
    GoodsType.objects.create(type_label="海鲜水产",type_description="海鲜水产",type_picture="img/banner02.jpg")
    GoodsType.objects.create(type_label="猪牛羊肉",type_description="猪牛羊肉",type_picture="img/banner03.jpg")
    GoodsType.objects.create(type_label="禽类蛋品",type_description="禽类蛋品",type_picture="img/banner04.jpg")
    GoodsType.objects.create(type_label="新鲜蔬菜",type_description="新鲜蔬菜",type_picture="img/banner05.jpg")
    GoodsType.objects.create(type_label="速冻食品",type_description="速冻食品",type_picture="img/banner06.jpg")

    return HttpResponse("添加成功")

from sdk.send163 import sendQQ_Email
from CeleryTask.tasks import send_yibu_163
def get_code(request):
    result = {"code":10000,"msg":"验证码已发送,注意查收"}
    ##发送验证码
    email = request.GET.get("email")
    user_email = ValidCode.objects.create()
    print(email,user_email)
    code = random.randint(10000,99999)
    params = {
        "content":"您的验证码为:{},请注意邮箱进行查收".format(code),
        "recver": email,
    }
    try:
        # sendQQ_Email(params)
        # send_yibu_163(params)    ##异步任务
        ##存储到数据库
        user_email.user = "{}".format(email)
        user_email.code = "{}".format(code)
        user_email.save()
        result = {"code":10000, "msg": "验证码已发送,注意查收"}
    except:
        result = {"code": 10001, "msg": "验证码发送失败"}

    return JsonResponse(result)



def middlewaretest(request,version):
    print("view")
    def test01():
        return HttpResponse("test")
    resp = HttpResponse("middlewaretest")
    resp.render = test01
    return resp



