# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='input_formats',
            field=models.BooleanField(default=False, verbose_name=b'\xe6\x96\x87\xe6\x9c\xac\xe6\xa0\xbc\xe5\xbc\x8f'),
            preserve_default=True,
        ),
    ]
