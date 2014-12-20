# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns

urlpatterns = patterns('',
                       url(r'^login/$', 'accounts.views.login_view'),
                       url(r'^auth/$', 'accounts.views.auth_view'),
                       url(r'^logout/$', 'accounts.views.logout_view'),
                       url(r'^loggedin/$', 'accounts.views.loggedin_view'),
                       url(r'^invalid/$', 'accounts.views.invalid_view'),
                       url(r'^register/$', 'accounts.views.register_user'),
                       url(r'^register_success/$', 'accounts.views.register_success'),
                       )