from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def queryfunc(request):
    '''获取前段传入的查询字符串参数'''

    # 获取参数
    queryDict = request.GET

    # 从特殊的dict中获取数据
    a = queryDict.get('a')
    b = queryDict.get('b')
    alist = queryDict.getlist('a')

    # 打印
    print(a)
    print(b)
    print(alist)

    # 返回
    return HttpResponse('queryfunc')


def routerfunc(request, city, year):
    '''获取前段传入的路径参数'''

    print(city)
    print(year)
    return HttpResponse('routefunc')


def routerfunc1(request, year, city):
    '''获取前端传入的路径参数'''
    print(city)
    print(year)
    return HttpResponse('routerfunc')


def formfunc(request):
    '''接受前端传入的表单参数'''
    a = request.POST.get('a')
    b = request.POST.get('b')
    alist = request.POST.getlist('a')

    print(a)
    print(b)
    print(alist)

    return HttpResponse('formfunc')