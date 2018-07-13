"""hno_lehrprogramm URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from hno_lehrprogramm.views import start
from ubung.views import showbild, ubungTest
from lernen.views import article
from supuser.views import supauser
from django.conf import settings
from django.views.static import serve
import object_tools
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', start),
    url(r'^start/$', start),
    url(r'^bild/$', showbild),
    url(r'^lernen/', article),
    url(r'^ubung/', ubungTest),
    url(r'^login/$', login, {'template_name': 'login.html'}),
    url(r'^login/superuser/', supauser),
]

if settings.DEBUG:
    urlpatterns += [url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }), ]
