# -*- coding: utf-8 -*-
from django.contrib import admin
from article.models import Article, Comment
# Register your models here.


# class CommentInline(admin.TabularInline):
#     model = Comment
#     extra = 3
#
#
# class ArticleAdmin(admin.ModelAdmin):
#     fieldsets = [(None, {'fields': ['title']}), ]
#     inlines = [CommentInline]


admin.site.register(Article)
admin.site.register(Comment)
