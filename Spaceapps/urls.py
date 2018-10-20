from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from home import views

urlpatterns = [
    url(r'^$',views.index,name="index"),
   # url(r'^page',views.Sample,name="Sample Page"),
]
