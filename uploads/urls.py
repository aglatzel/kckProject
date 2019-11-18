from django.conf.urls import url
from django.contrib import admin

from uploads.core import views


urlpatterns = [
    url('^$', views.home, name='home'),
    url('send_name/', views.send_name, name='send_name'),
    url('about/', views.about, name='about'),
]
