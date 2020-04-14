from django.urls import re_path
from .import views

urlpatterns = [
    re_path(r'^setcook/$',views.setcookfunc),
    re_path(r'^getcook/$',views.getcookfunc),
]
