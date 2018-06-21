from django import template
from django.shortcuts import get_object_or_404
from scrum.models import Skill
register = template.Library()

@register.filter
def java (value):
    try:
        if value.skillSet.get(name="Java") is not None:
            return value.skillSet.get(name="Java").proficiency
    except:
        return ""


@register.filter
def python (value):
    try:
        if value.skillSet.get(name="Python") is not None:
            return value.skillSet.get(name="Python").proficiency
    except:
        return ""


@register.filter
def c (value):
    try:
        if value.skillSet.get(name="C") is not None:
            return value.skillSet.get(name="C").proficiency
    except:
        return ""


@register.filter
def c_plus (value):
    try:
        if value.skillSet.get(name="C++") is not None:
            return value.skillSet.get(name="C++").proficiency
    except:
        return ""


@register.filter
def c_sharp (value):
    try:
        if value.skillSet.get(name="C#") is not None:
            return value.skillSet.get(name="C#").proficiency
    except:
        return ""


@register.filter
def sql (value):
    try:
        if value.skillSet.get(name="SQL") is not None:
            return value.skillSet.get(name="SQL").proficiency
    except:
        return ""



@register.filter
def mysql (value):
    try:
        if value.skillSet.get(name="MySQL") is not None:
            return value.skillSet.get(name="MySQL").proficiency
    except:
        return ""


@register.filter
def mongodb (value):
    try:
        if value.skillSet.get(name="MongooDB") is not None:
            return value.skillSet.get(name="MongooDB").proficiency
    except:
        return ""

@register.filter
def marketing (value):
    try:
        if value.skillSet.get(name="Marketing") is not None:
            return value.skillSet.get(name="Marketing").proficiency
    except:
        return ""


@register.filter
def analytics (value):
    try:
        if value.skillSet.get(name="Analytics") is not None:
            return value.skillSet.get(name="Analytics").proficiency
    except:
        return ""

@register.filter
def web(value):
    try:
        if value.skillSet.get(name="Web") is not None:
            return value.skillSet.get(name="Web").proficiency
    except:
        return ""


@register.filter
def design(value):
    try:
        if value.skillSet.get(name="Design") is not None:
            return value.skillSet.get(name="Design").proficiency
    except:
        return ""


@register.filter
def agile (value):
    try:
        if value.skillSet.get(name="Agile") is not None:
            return value.skillSet.get(name="Agile").proficiency
    except:
        return ""


@register.filter
def c_sharp (value):
    try:
        if value.skillSet.get(name="Java") is not None:
            return value.skillSet.get(name="Java").proficiency
    except:
        return ""

@register.filter
def c_sharp (value):
    try:
        if value.skillSet.get(name="Java") is not None:
            return value.skillSet.get(name="Java").proficiency
    except:
        return ""
