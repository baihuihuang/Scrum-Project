# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-13 19:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('scrum', '0002_auto_20180612_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 13, 19, 24, 54, 100010, tzinfo=utc)),
        ),
    ]