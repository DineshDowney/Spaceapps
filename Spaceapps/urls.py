from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.index,name="index"),
   # url(r'^page',views.Sample,name="Sample Page"),
  # url(r'^upload/$',views.upload,name="upload"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)