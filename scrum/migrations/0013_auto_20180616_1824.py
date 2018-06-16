# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-16 18:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('scrum', '0012_auto_20180615_2252'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='timeZone',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 16, 18, 24, 38, 858623, tzinfo=utc)),
        ),
    ]