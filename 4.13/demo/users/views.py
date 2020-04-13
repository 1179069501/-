from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse


def haha(request):
    print("haha函数")
    return HttpResponse('haha函数')


def index(request):
    """
    index视图
    :param request:包含了请求信息的请求对象
    :return: 响应对象
    """
    print('index函数')
    # a = 1/0
    return HttpResponse("index函数")

def say(request):
    '''say'''
    print('say')

    url = reverse('uu:index')
    print(url)
    return redirect(url)

def sayhello(request):
    """sayhello"""

    print('sayhello')

    return HttpResponse('sayhello')





