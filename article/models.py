# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
import datetime



# Create your models here.


class Article(models.Model):
    """ 文章
    """
    title = models.CharField(max_length=50, verbose_name='标题')
    body = models.TextField(verbose_name='内容')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='提交时间')
    likes = models.IntegerField(verbose_name='赞', default=0)
    image = models.ImageField(verbose_name='图片', upload_to='uploads', blank=True)
    author = models.CharField(verbose_name='名字', max_length=10)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'
        ordering = ['-pub_date']


class Comment(models.Model):
    """ 评论
    """
    name = models.CharField(max_length=50, verbose_name='名字')
    body = models.TextField(verbose_name='内容')
    pub_date = models.DateTimeField()
    article = models.ForeignKey(Article)
    approved = models.BooleanField(default=True, verbose_name='已审核')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = '评论'
        ordering = ['-pub_date']

