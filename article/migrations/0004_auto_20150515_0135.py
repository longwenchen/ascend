# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20141216_0223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='body',
            field=django_markdown.models.MarkdownField(verbose_name=b'\xe5\x86\x85\xe5\xae\xb9'),
        ),
    ]
