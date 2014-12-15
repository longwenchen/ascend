# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_article_input_formats'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content_type',
            field=models.CharField(default=b'topic', max_length=10, verbose_name=b'\xe5\x86\x85\xe5\xae\xb9\xe7\xb1\xbb\xe5\x9e\x8b'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.CharField(max_length=25, verbose_name=b'\xe5\x90\x8d\xe5\xad\x97'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='input_formats',
            field=models.BooleanField(default=False, verbose_name=b'\xe5\xaf\x8c\xe6\x96\x87\xe6\x9c\xac\xe6\xa0\xbc\xe5\xbc\x8f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=25, verbose_name=b'\xe5\x90\x8d\xe5\xad\x97'),
            preserve_default=True,
        ),
    ]
