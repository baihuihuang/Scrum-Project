# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-13 20:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('scrum', '0003_auto_20180613_1924'),
    ]

    operations = [
        migrations.CreateModel(
            name='MinSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=b'null', max_length=50)),
                ('proficiency', models.IntegerField(default=0)),
                ('yrOfExperience', models.IntegerField(blank=True, default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='manager',
            name='numberOfTeam',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='manager',
            name='numberPPlOfTeam',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 13, 20, 46, 11, 342943, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='minskill',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scrum.Profile'),
        ),
    ]
