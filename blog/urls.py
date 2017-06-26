from django.conf.urls import url

from . import admin, views

from .views import (
    blog_list,
    blog_detail,
    blog_update, 
    blog_create,
    blog_delete
)

urlpatterns = [
    url(r'^$', blog_list),
    url(r'^create/', blog_create),
    url(r'^update/', blog_update),
    # this is used for letting the url decide which blog
    # id to open
    # apprently it needs to be name="thing"
    url(r'^(?P<id>\d+)/$', blog_detail, name="blog_detail"),
    url(r'^delete/', blog_delete),
]
