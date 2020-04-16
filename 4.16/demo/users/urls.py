from django.conf.urls import re_path
from . import views


app_name = 'uu'

urlpatterns = [
    re_path(r'^index/$',views.index),
    re_path(r'^sayhello',views.sayhello),
    re_path(r'^say',views.say),

]