from django.urls import re_path
from .import views

urlpatterns = [
    re_path(r'^query/$',views.queryfunc),
    # re_path(r'^weather/([a-z]+)/(\d{4})/$',views.routerfunc),
    re_path(r'^weather/(?P<city>[a-z]+)/(?P<year>\d{4})/$',views.routerfunc1),
    re_path(r'^form/$',views.formfunc),
    re_path(r'^json/$',views.jsonfunc),
    re_path(r'^response/$',views.responsefunc),
    re_path(r'^jsonfunc/$',views.jsonFunc),
]
