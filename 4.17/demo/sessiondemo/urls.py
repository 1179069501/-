from django.urls import re_path
from .import views

urlpatterns = [
    re_path(r'^setsession/$',views.setsessionfunc),
    re_path(r'^getsession/$',views.getsessionfunc),
]
