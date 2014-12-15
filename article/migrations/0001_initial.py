# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('body', models.TextField(verbose_name=b'\xe5\x86\x85\xe5\xae\xb9')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe6\x8f\x90\xe4\xba\xa4\xe6\x97\xb6\xe9\x97\xb4')),
                ('likes', models.IntegerField(default=0, verbose_name=b'\xe8\xb5\x9e')),
                ('image', models.ImageField(upload_to=b'uploads', verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87', blank=True)),
                ('author', models.CharField(max_length=10, verbose_name=b'\xe5\x90\x8d\xe5\xad\x97')),
            ],
            options={
                'ordering': ['-pub_date'],
                'verbose_name': '\u6587\u7ae0',
                'verbose_name_plural': '\u6587\u7ae0',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'\xe5\x90\x8d\xe5\xad\x97')),
                ('body', models.TextField(verbose_name=b'\xe5\x86\x85\xe5\xae\xb9')),
                ('pub_date', models.DateTimeField()),
                ('approved', models.BooleanField(default=True, verbose_name=b'\xe5\xb7\xb2\xe5\xae\xa1\xe6\xa0\xb8')),
                ('article', models.ForeignKey(to='article.Article')),
            ],
            options={
                'ordering': ['-pub_date'],
                'verbose_name': '\u8bc4\u8bba',
                'verbose_name_plural': '\u8bc4\u8bba',
            },
            bases=(models.Model,),
        ),
    ]
