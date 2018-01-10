# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-05 12:21
from __future__ import unicode_literals

import time

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('fitapp', '0006_help_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='userfitbit',
            name='expires_at',
            field=models.FloatField(default=time.time(),
                                    help_text=b'The timestamp when the access token expires'),
            preserve_default=False,
        ),
    ]
