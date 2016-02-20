"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
# coding=utf8
# -*- coding: utf8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.conf.urls import patterns, include, url, static
from django.contrib import admin
from app.views import *

urlpatterns = [
    url(r'^$', landing, name ='landing'),
    url(r'^promos$', promos, name = 'promos'),
    url(r'^wishes$', wishes, name = 'wishes'),
    url(r'^make-wish$', makeawish, name = 'MakeAWish'),
    url(r'^admin/', admin.site.urls),

    #info and verification
    url(r'^robots.txt$', robots, name = 'robots.txt'),
    url(r'^sitemap$', sitemap, name = 'sitemap'),
    #url(r'^google74b8934454bd29ba.html$', google, name = 'Google Verification'),
    #url(r'^BingSiteAuth.xml$', bing, name = 'Bing Verification'),
]

#if settings.DEBUG:
    #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)