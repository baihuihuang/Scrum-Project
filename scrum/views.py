from django.shortcuts import render

# Create your views here.
from scrum.models import *
from scrum.forms import ProfileForm, SkillForm, TeamForm,  ManagerForm
from django.http import Http404


def home(request):
    context = {}
    context['form'] = ProfileForm()
    context['skill'] = SkillForm()
    return render(request, 'home.html', context)


def create_manager(request):
    pass


def create_profile(request):
    context = {}
    try:
        if request.method == 'POST':
            profile = Profile.objects.create()
            form = ProfileForm(request.POST, instance=profile)
            if form.is_valid():
                form.save()
                profile.save()
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
            # manager = Manager.objects.create()
            # form = ProfileForm(request.POST, instance=manager)
            # if form.is_valid():
            #     form.save()
            #     manager.save()
            #     context['msg'] = "Submitted successful"
            #     context['form'] = ProfileForm()
            #     print("form is saved")
            # else:
            #     context['msg'] = "Check your data"
            #     print("form not valid")
            return render(request, 'manager.html', context)
        else:
            context['form'] = ManagerForm()
            return render(request, 'manager.html', context)

    except:
        print("error")
        raise Http404
    return render(request, 'manager.html', context)
