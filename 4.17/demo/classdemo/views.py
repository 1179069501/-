from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View



#定义一个装饰器：
# def my_decorator(func):
#     def wrapper(self,request,*args,**kwargs):
#         print('请求路径：%s'%request.path)
#         print('装饰器函数调用')
#         return func(self,request,*args,**kwargs)
#     return wrapper

def my_decorator(func):
    def wrapper(request,*args,**kwargs):
        print('请求路径：%s'%request.path)
        print('装饰器函数调用')
        return func(request,*args,**kwargs)
    return wrapper

def my_decorator1(func):
    def wrapper(request,*args,**kwargs):
        print('请求路径：%s'%request.path)
        print('装饰器函数调用')
        return func(request,*args,**kwargs)
    return wrapper


class FirstMixin(object):

    @classmethod
    def as_view(cls,*args,**kwargs):
        view = super().as_view(*args,**kwargs)
        return my_decorator(view)

class SecondMixin(object):

    @classmethod
    def as_view(cls,*args,**kwargs):
        view = super().as_view(*args,**kwargs)
        return my_decorator1(view)

# @method_decorator(my_decorator,name='dispathch')
class RegisterView(FirstMixin,SecondMixin,View):

    # @my_decorator
    # @method_decorator(my_decorator)
    def get(self,request):
        print('RegisterView get')
        return HttpResponse('RegisterView get')

    def set(self,request):
        print('RegisterView set')
        return HttpResponse('RegisterView set')



