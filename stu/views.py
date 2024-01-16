from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index_view(request):
    return render(request, 'login.html')

def login_view(request):

    uname = request.GET.get('uname', '')
    pwd = request.GET.get('pwd', '')

    if uname == 'zhangsan' and pwd == '123':
        return HttpResponse('登录成功')
    return HttpResponse('登录失败')
