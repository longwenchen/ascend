# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from models import Article
from forms import ArticleForm, CommentForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.utils import timezone
from django.views.decorators.cache import cache_page

# Create your views here.


# @cache_page(60 * 15)
def index(request):
    """ 首页: 显示文章列表
    """
    articles = Article.objects.filter(content_type='topic')
    return render(request, 'article/index.html', locals())


# @cache_page(60 * 15)
def hlp(request):
    """ 帮助: 显示文章列表
    """
    articles = Article.objects.filter(content_type='hlp')
    return render(request, 'article/index.html', locals())


# @cache_page(60 * 15)
def detail(request, article_id=1):
    """ 内容页: 显示详细文章内容和评论
    """
    article = Article.objects.get(id=article_id)

    return render(request, 'article/detail.html', locals())

# @cache_page(60 * 15)
def about(request):
    return render(request, 'about.html')


def create(request):
    if request.POST:
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ArticleForm()

    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render_to_response('article/create_article.html', args)


def add_comment(request, article_id):
    a = Article.objects.get(id=article_id)

    if request.POST:
        f = CommentForm(request.POST)
        if f.is_valid():
            c = f.save(commit=False)
            c.pub_date = timezone.now()
            c.article = a
            c.save()

            return HttpResponseRedirect('/node/%s' % article_id)
    else:
        f = CommentForm()

    args = {}
    args.update(csrf(request))

    args['article'] = a
    args['form'] = f

    return render_to_response('article/add_comment.html', args)





