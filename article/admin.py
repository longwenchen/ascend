# -*- coding: utf-8 -*-
from django.contrib import admin
from article.models import Article, Comment
from django_markdown.admin import MarkdownModelAdmin
# Register your models here.


# class CommentInline(admin.TabularInline):
#     model = Comment
#     extra = 3
#
#
# class ArticleAdmin(admin.ModelAdmin):
#     formfield_overrides = {MarkdownField: {'widget': AdminMarkdownWidget}}
    # fieldsets = [(None, {'fields': ['title']}), ]
    # inlines = [CommentInline]


admin.site.register(Article, MarkdownModelAdmin)
admin.site.register(Comment)
