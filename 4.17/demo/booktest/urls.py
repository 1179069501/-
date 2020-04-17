from django.urls import re_path
from .import views

urlpatterns = [
    re_path(r'^booktest/$',views.SaveDataView.as_view()),
]
