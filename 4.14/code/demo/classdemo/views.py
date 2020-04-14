from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View


class RegisterView(View):
    def get(self,request):
        print('RegisterView get')
        return HttpResponse('RegisterView get')

    def set(self,request):
        print('RegisterView set')
        return HttpResponse('RegisterView set')