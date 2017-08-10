"""personalsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
# as of django 1.10 you must import the function
# and pass that in
from blog import views as blog_view
from blog.views import contact_me
from blog.views import project_list
from django.views.generic.base import RedirectView

# TAKES THIS OUT BEFORE PRODUCTION
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', RedirectView.as_view(url="/blog/", permanent=True)),
    url(r'^contact$', RedirectView.as_view(url="/whoami", permanent=True)),
    url(r'^blog/', include("blog.urls"), name="home"),
    url(r'^projects/', project_list, name="project_list"),
    #url(r'^blog/$', <function_name>) after you have imported the function
    url(r'whoami/', contact_me, name="whoami"),
]

# as of django 1.10 this is not correct
#url(r'^blog/$', "<appname>.views.<function_name")
