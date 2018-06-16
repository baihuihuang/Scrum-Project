from django.core.exceptions import ValidationError
from django.shortcuts import render

# Create your views here.
from scrum.models import *
from scrum.forms import ProfileForm, SkillForm, ManagerForm, MinSkillForm
from django.http import Http404
from django.forms import modelformset_factory


def home(request):
    context = {}
    context['people'] = Profile.objects.all()
    return render(request, 'home.html', context)


def create_profile(request):
    context = {}
    profile = Profile.objects.create()
    form = ProfileForm(request.POST, instance=profile)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            profile.save()
            skill = Skill.objects.create(profile=profile)
            SkillFormSet = modelformset_factory(Skill, form=SkillForm)
            try:
                formset = SkillFormSet(request.POST)
            except ValidationError:
                formset = None

            formset.save()
            print(formset.has_changed())
            print("sForm save")
            context['msg'] = "Submitted successful"
            context['form'] = ProfileForm()
            context['skills'] = modelformset_factory(Skill, form=SkillForm, extra=5)
            context['secSkills'] = modelformset_factory(Skill, form=SkillForm, extra=5)
            print("form is saved")
        else:
            context['msg'] = "Check your data"
            print("form not valid")
    else:
        context['form'] = ProfileForm()
        context['skills'] = modelformset_factory(Skill, form=SkillForm)
        context['secSkills'] = modelformset_factory(Skill, form=SkillForm)
    return render(request, 'profile.html', context)

    #
    # try:
    #     if request.method == 'POST':
    #         profile = Profile.objects.create()
    #         form = ProfileForm(request.POST, instance=profile)
    #         if form.is_valid():
    #             form.save()
    #             profile.save()
    #             skill = Skill.objects.create(profile=profile)
    #             SkillFormSet = modelformset_factory(Skill)
    #             formset = SkillFormSet(request.POST)
    #             if formset.is_valid():
    #                 formset.save()
    #             print("sForm save")
    #             context['msg'] = "Submitted successful"
    #             context['form'] = ProfileForm()
    #             context['skills'] = modelformset_factory(SkillForm,extra=5)
    #             context['secSkills'] = modelformset_factory(SkillForm,extra=5)
    #             print("form is saved")
    #         else:
    #             context['msg'] = "Check your data"
    #             print("form not valid")
    #         return render(request, 'home.html', context)
    #     else:
    #         context['form'] = ProfileForm()
    #         return render(request, 'test_form.html', context)
    # except:
    #     print("error")
    #     raise Http404
    # return render(request, 'test_form.html', context)


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


# def match_team(request):
#     context = {}
#     manager = Manager.objects.create()
#     min_skill = MinSkill.objects.create()
#
#     if request.method == 'POST':
#         form = ManagerForm(request.POST, instance=manager)
#         minSForm = MinSkillForm(request.POST, instance=min_skill)
#         minSForm.save()
#         min_skill.save()
#         numTeam = form.data['numberOfTeam']
#         numPeo = form.data['numberPPlOfTeam']
#         skill = minSForm.data['name']
#         pro = minSForm.data['proficiency']
#         yr = minSForm.data['yrOfExperience']
#         print(pro)
#         print(skill)
#         print(yr)
#         candidate = Skill.objects.filter(name=skill, proficiency__gt=pro,yrOfExperience__gt=yr)
#         context['people'] = candidate
#         context['minForm'] = MinSkillForm()
#         return render(request, 'manager.html', context)
#     else:
#         context['minForm'] = MinSkillForm()
#         context['form'] = ManagerForm()
#         return render(request, 'manager.html', context)
#     # try:
#     #     manager = Manager.objects.create()
#     #     if request.method == 'POST':
#     #         form = ManagerForm(request.POST, instance=manager)
#     #         print (form.numberOfTeam)
#     #         return render(request, 'manager.html', context)
#     #     else:
#     #         context['minForm'] = MinSkillForm()
#     #         context['form'] = ManagerForm()
#     #         return render(request, 'manager.html', context)
#     #
#     # except:
#     #     print("error")
#     #     raise Http404
#     return render(request, 'manager.html', context)

def match_team(request):
    context = {}
    manager = Manager.objects.create()
    min_skill = MinSkill.objects.create()

    if request.method == 'POST':

        # all the value from team1
        name_skill1_team1 = request.POST["name_skill1_team1"]
        proficiency_skill1_team1 = request.POST["proficiency_skill1_team1"]
        yr_skill1_team1 = request.POST["yr_skill1_team1"]
        candidate_1 = Skill.objects.filter(name=name_skill1_team1, proficiency__gt=proficiency_skill1_team1,
                                           yrOfExperience__gt=yr_skill1_team1)
        for c in candidate_1:
            print(c.name)
        if 'name_skill2_team1' in request.POST:
            name_skill2_team1 = request.POST["name_skill2_team1"]
            proficiency_skill2_team1 = request.POST["proficiency_skill2_team1"]
            yr_skill2_team1 = request.POST["yr_skill2_team1"]
            candidate_2 = Skill.objects.filter(name=name_skill2_team1, proficiency__gt=proficiency_skill2_team1,
                                               yrOfExperience__gt=yr_skill2_team1)
            for c in candidate_2:
                print(c.name)


        # pro = minSForm.data['proficiency']
        # yr = minSForm.data['yrOfExperience']
        # print(yr)
        # candidate = Skill.objects.filter(name=skill, proficiency__gt=pro,yrOfExperience__gt=yr)
        # context['people'] = candidate
        # context['minForm'] = MinSkillForm()

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
