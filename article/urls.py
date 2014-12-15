# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url


urlpatterns = patterns('',
                        url(r'^node/(?P<article_id>\d+)/$', 'article.views.detail', name="detail"),
                        url(r'^article/create/$', 'article.views.create'),
                        url(r'^article/add_comment/(?P<article_id>\d+)/$', 'article.views.add_comment'),
                        url(r'^$', 'article.views.index'),
                       )