from django.shortcuts import render
import json
# Create your views here.
from django.http import HttpResponse,HttpResponseBadRequest,JsonResponse

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


def jsonfunc(request):
    """json传参"""
    dict = json.loads(request.body.decode())
    a =  dict.get('a')
    b =  dict.get('b')

    #获取请求头信息：
    print(request.META.get('CONTENT_LENGTH'))
    print(request.user)
    print(request.path)
    print(request.method)

    # return HttpResponse('jsonfunc',
    #                     content_type='application/json',
    #                     status=404)

    response = HttpResponse('jsonfunc')

    response['itcast'] = 'python'


    return response





def responsefunc(request):
    print('responsefunc')

    return HttpResponseBadRequest('responsefunc')

def jsonFunc(request):
    # print('jsonFunc')
    #
    # dict = {
    #     'name':'zs',
    #     'age':123
    # }
    #
    # return JsonResponse(dict)

    list = [{
        'name':'zs',
        'age':123
    }]
    return JsonResponse(list,safe=False)