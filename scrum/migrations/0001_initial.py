# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-10 16:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numberOfTeam', models.IntegerField(default=10)),
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
                ('yrOfExperience', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('proficiency', models.IntegerField(max_length=3)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='have_skill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='have_skill', to='scrum.Skill'),
        ),
    ]
