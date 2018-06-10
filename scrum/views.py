from django.shortcuts import render

# Create your views here.
from scrum.models import *
from scrum.forms import ProfileForm

def home(request):
    context = {}
    context['form'] = ProfileForm()
    return render(request, 'home.html', context)
