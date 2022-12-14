from django.shortcuts import render, HttpResponse, redirect
from app01.models import Department, UserInfo


# Create your views here.
def index(request):
    return HttpResponse("欢迎使用")


def user_list(request):
    return render(request, "user_list.html")


def user_add(request):
    return render(request, "user_add.html")


def tpl(request):
    return render(request, "tpl.html")


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        username = request.POST.get("user")
        password = request.POST.get("pwd")

        if username == 'root' and password == "123":
            return redirect("https://www.baidu.com/")
        else:
            return render(request, "login.html", {"error_msg": "用户名或者密码错误"})


def orm(request):
    """
    Department.objects.create(title="销售部")
    Department.objects.create(title="企划部")
    Department.objects.create(title="IT部")
    :param request:
    :return:
    """
    #    UserInfo.objects.create(name="大多", password="666", age=16)
    #    UserInfo.objects.create(name="金多", password="999", age=15)
    #   UserInfo.objects.filter(id=3).delete()
    """
    data_list = UserInfo.objects.all()
    for obj in data_list:
        print(obj.name, obj.password, obj.age)
    """
    # UserInfo.objects.filter(name="金多").update(age=9)
    UserInfo.objects.create(name="阿多", password="666", age=16)

    return HttpResponse("成功")


def info_list(request):
    # 数据库中的用户信息
    data_list = UserInfo.objects.all()

    return render(request, "info_list.html", {"data_list": data_list})


def info_add(request):
    if request.method == "GET":
        return render(request, 'info_add.html')
    # 获取到网页填入的信息
    user = request.POST.get("user")
    pwd = request.POST.get("pwd")
    age = request.POST.get("age")
    # 网数据库添加信息
    UserInfo.objects.create(name=user, password=pwd, age=age)

    return redirect("/info/list/")


def info_delete(request):
    nid = request.GET.get("nid")
    UserInfo.objects.filter(id=nid).delete()
    return redirect("/info/list/")
