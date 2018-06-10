from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class Skill(models.Model):
    name = models.CharField(blank=True, null=True, max_length=50)
    proficiency = models.IntegerField()


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
    yrOfExperience = models.IntegerField()
    have_skill = models.ForeignKey(Skill, related_name="have_skill", on_delete=models.CASCADE)
    phone = models.CharField(blank=True, null=True, max_length=50)
    email = models.CharField(blank=True, null=True, max_length=50)
    created_at = models.DateTimeField(default=timezone.now())


class Manager(models.Model):
    numberOfTeam = models.IntegerField(default=10)


