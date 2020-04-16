from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def setcookfunc(request):
    response = HttpResponse('setcookfunc')
    # response.set_cookie('key','value','有效期')
    response.set_cookie('itcast','python',max_age=3600*24*14)

    return response

def getcookfunc(request):
    '''读取cookie的值'''
    value = request.COOKIES.get('itcast')
    print(value)

    return HttpResponse('value')