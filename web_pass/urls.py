# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from webpassapp.views import main_page
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'web_pass.views.home', name='home'),
    # url(r'^web_pass/', include('web_pass.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    ('^$', main_page),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/mak/devel/django_exp/virtualenv/test_comments/web_pass/web_pass/static'}),
)
