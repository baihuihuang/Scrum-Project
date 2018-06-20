# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-18 01:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('scrum', '0016_auto_20180618_0102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='pSkillCount',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='sSkillCount',
        ),
        migrations.AddField(
            model_name='profile',
            name='pSkillCount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='sSkillCount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 18, 1, 4, 24, 884745, tzinfo=utc)),
        ),
    ]