from django.conf.urls import url

from . import admin, views

urlpatterns = [
    url(r'^$', views.index, name="index"),
]
