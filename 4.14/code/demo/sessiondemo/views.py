from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def setsessionfunc(request):
    """设置session数据"""

    #设置session数据
    request.session['itcast123']= 'python123'
    return HttpResponse("setsessionfunc")

def getsessionfunc(request):
    value = request.session['itcast123']
    print(value)

    return HttpResponse('getsessionfunc')
