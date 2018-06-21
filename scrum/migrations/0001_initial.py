# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-18 02:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numberOfTeam', models.IntegerField(null=True)),
                ('numberPPlOfTeam', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MinSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=b'null', max_length=50)),
                ('proficiency', models.IntegerField(default=0)),
                ('yrOfExperience', models.IntegerField(blank=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(blank=True, max_length=50, null=True)),
                ('lastName', models.CharField(blank=True, max_length=50, null=True)),
                ('department', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('availability', models.CharField(choices=[(b'YES', b'Yes'), (b'NO', b'No')], max_length=3)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2018, 6, 18, 2, 35, 8, 280731, tzinfo=utc))),
                ('timeZone', models.CharField(blank=True, max_length=50, null=True)),
                ('pSkillCount', models.IntegerField(default=0)),
                ('sSkillCount', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=b'null', max_length=50)),
                ('proficiency', models.IntegerField(default=0)),
                ('yrOfExperience', models.IntegerField(blank=True, default=0)),
                ('type', models.CharField(blank=True, max_length=1, null=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skillSet', to='scrum.Profile')),
            ],
        ),
    ]
