# -*- coding: utf-8 -*-
from django.forms import forms, ModelForm, Textarea
from models import Article, Comment


class ArticleForm(ModelForm):

    class Meta:
        model = Article
        fields = ('author', 'title', 'body', 'image')
        widgets = {'title': Textarea(attrs={'class': "form-control", 'rows': 1}),
                   'body': Textarea(attrs={'class': "form-control"}),
                   'author': Textarea(attrs={'class': "form-control", 'rows': 1})}


class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ('name', 'body')
        widgets = {'name': Textarea(attrs={'class': "form-control", 'rows': 1}),
                   'body': Textarea(attrs={'class': "form-control"})}
