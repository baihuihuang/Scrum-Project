from django.core.exceptions import ValidationError
from django.shortcuts import render

# Create your views here.
from scrum.models import *
from scrum.forms import ProfileForm, SkillForm, ManagerForm, MinSkillForm
from django.http import Http404
from django.forms import modelformset_factory
from django import template

register = template.Library()


def home(request):
    context = {}
    context['people'] = Profile.objects.all()
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


def match_team(request):
    context = {}
    manager = Manager.objects.create()

    if request.method == 'POST':
        # get the manager input
        form = ManagerForm(request.POST, instance=manager)
        numberOfPeople = form.data['numberPPlOfTeam']
        form.save()

        # all the value from team1
        name_skill1_team1 = request.POST["name_skill1_team1"]
        proficiency_skill1_team1 = request.POST["proficiency_skill1_team1"]
        yr_skill1_team1 = request.POST["yr_skill1_team1"]
        candidate_1 = Skill.objects.filter(name=name_skill1_team1, proficiency__gt=proficiency_skill1_team1,
                                           yrOfExperience__gt=yr_skill1_team1)
        candidate_2 = None

        if 'name_skill2_team1' in request.POST and 'name_skill1_team2' not in request.POST:
            name_skill2_team1 = request.POST["name_skill2_team1"]
            proficiency_skill2_team1 = request.POST["proficiency_skill2_team1"]
            yr_skill2_team1 = request.POST["yr_skill2_team1"]
            candidate_2 = Skill.objects.filter(name=name_skill2_team1, proficiency__gt=proficiency_skill2_team1,
                                               yrOfExperience__gt=yr_skill2_team1)

        if candidate_2 is None and candidate_1 is not None:
            candidate_1 = candidate_1.order_by('proficiency', 'yrOfExperience')[:int(numberOfPeople)]
            context['people'] = candidate_1
        elif candidate_1 is None and candidate_2 is not None:
            candidate_2 = candidate_2.order_by('proficiency', 'yrOfExperience')[:int(numberOfPeople)]
            context['people'] = candidate_2
        elif candidate_1 is not None and candidate_2 is not None:
            candidate_1 = candidate_1.order_by('proficiency', 'yrOfExperience')[:int(numberOfPeople)]
            candidate_2 = candidate_2.order_by('proficiency', 'yrOfExperience')[:int(numberOfPeople)]
            candidate_all = list(
                set(candidate_1.values_list('profile')).intersection(candidate_2.values_list('profile')))
            candidate_all = [c[0] for c in candidate_all]
            p = Profile.objects.filter(id__in=candidate_all)[:int(numberOfPeople)]
            context['ppl'] = p


        context['minForm'] = MinSkillForm()
        context['form'] = ManagerForm()

        return render(request, 'manager.html', context)
    else:
        context['minForm'] = MinSkillForm()
        context['form'] = ManagerForm()
        return render(request, 'manager.html', context)

    return render(request, 'manager.html', context)

@register.filter(name='cut')
def cut(value):
    return value.length
