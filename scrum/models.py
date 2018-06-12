from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class Profile(models.Model):
    AVA_OPTION = (
        ('YES', 'Yes'),
        ('NO', 'No')
    )
    firstName = models.CharField(blank=True, null=True, max_length=50)
    lastName = models.CharField(blank=True, null=True, max_length=50)
    department = models.CharField(blank=True, null=True, max_length=50)
    city = models.CharField(blank=True, null=True, max_length=50)
    availability = models.CharField(max_length=3, choices=AVA_OPTION)
    phone = models.CharField(blank=True, null=True, max_length=50)
    email = models.CharField(blank=True, null=True, max_length=50)
    created_at = models.DateTimeField(default=timezone.now())


class Skill(models.Model):
    name = models.CharField(blank=True, null=True, max_length=50)
    proficiency = models.IntegerField()
    yrOfExperience = models.IntegerField(blank=True)
    profile = models.ForeignKey(Profile)


class Manager(models.Model):
    numberOfTeam = models.IntegerField(default=10)


