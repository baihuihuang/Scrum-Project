from django.shortcuts import render

# Create your views here.
from scrum.models import *
from scrum.forms import ProfileForm, SkillForm, ManagerForm, MinSkillForm
from django.http import Http404


def home(request):
    context = {}
    context['form'] = ProfileForm()
    context['skill'] = SkillForm()
    return render(request, 'home.html', context)


def create_profile(request):
    context = {}

    try:
        if request.method == 'POST':
            profile = Profile.objects.create()
            form = ProfileForm(request.POST, instance=profile)
            if form.is_valid():
                form.save()
                profile.save()
                skill = Skill.objects.create(profile=profile)
                sForm = SkillForm(request.POST, instance=skill)
                sForm.save()
                print("sForm save")
                context['msg'] = "Submitted successful"
                context['form'] = ProfileForm()
                context['skill'] = SkillForm()
                print("form is saved")
            else:
                context['msg'] = "Check your data"
                print("form not valid")
            return render(request, 'home.html', context)
        else:
            context['form'] = ProfileForm()
            return render(request, 'home.html', context)
    except:
        print("error")
        raise Http404
    return render(request, 'home.html', context)


def create_manager(request):
    context = {}
    try:
        if request.method == 'POST':
            return render(request, 'manager.html', context)
        else:
            context['minForm'] = MinSkillForm()
            context['form'] = ManagerForm()
            return render(request, 'manager.html', context)

    except:
        print("error")
        raise Http404
    return render(request, 'manager.html', context)


def match_team(request):
    context = {}
    manager = Manager.objects.create()
    min_skill = MinSkill.objects.create()

    if request.method == 'POST':
        form = ManagerForm(request.POST, instance=manager)
        minSForm = MinSkillForm(request.POST, instance=min_skill)
        minSForm.save()
        min_skill.save()
        numTeam = form.data['numberOfTeam']
        numPeo = form.data['numberPPlOfTeam']
        skill = minSForm.data['name']
        pro = minSForm.data['proficiency']
        yr = minSForm.data['yrOfExperience']
        print(pro)
        print(skill)
        print(yr)
        candidate = Skill.objects.filter(name=skill, proficiency__gt=pro,yrOfExperience__gt=yr)
        context['people'] = candidate
        context['minForm'] = MinSkillForm()
        return render(request, 'manager.html', context)
    else:
        context['minForm'] = MinSkillForm()
        context['form'] = ManagerForm()
        return render(request, 'manager.html', context)
    # try:
    #     manager = Manager.objects.create()
    #     if request.method == 'POST':
    #         form = ManagerForm(request.POST, instance=manager)
    #         print (form.numberOfTeam)
    #         return render(request, 'manager.html', context)
    #     else:
    #         context['minForm'] = MinSkillForm()
    #         context['form'] = ManagerForm()
    #         return render(request, 'manager.html', context)
    #
    # except:
    #     print("error")
    #     raise Http404
    return render(request, 'manager.html', context)
