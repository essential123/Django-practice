from django.shortcuts import render, HttpResponse, redirect
from app01 import models


# Create your views here.

def userlist(request):
    data_queryset = models.Userinfo.objects.filter()
    return render(request, 'userlist.html', {'data_queryset': data_queryset})


def useradd(request):
    # 判断请求的方式
    if request.method == 'POST':
        name = request.POST.get('username')
        age = request.POST.get('age')
        # 判断用户名是否已存在
        user_obj = models.Userinfo.objects.filter(name=name)
        if user_obj:
            return HttpResponse('用户名已存在')
        # 写入数据库
        models.Userinfo.objects.create(name=name, age=age)
        # 跳转数据展示页
        return redirect('/userlist/')
    # 先返回一个添加用户数据的页面
    return render(request, 'useradd.html')


def useredit(request):
    edit_id = request.GET.get('id')
    if request.method == 'POST':
        name = request.POST.get('username')
        age = request.POST.get('age')
        print(name)
        print(age)
        models.Userinfo.objects.filter(id=edit_id).update(name=name, age=age)
        return redirect('/userlist/')
    edit_obj = models.Userinfo.objects.filter(id=edit_id).first()
    return render(request, 'useredit.html', {'edit_obj': edit_obj})


def userdelete(request):
    delete_id = request.GET.get('id')
    models.Userinfo.objects.filter(id=delete_id).delete()
    return redirect('/userlist/')
