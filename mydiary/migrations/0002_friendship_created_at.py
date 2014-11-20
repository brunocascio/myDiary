# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mydiary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='friendship',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 20, 0, 34, 35, 22634, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
