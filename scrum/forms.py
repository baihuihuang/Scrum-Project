from django import forms
from django.contrib.auth.models import User
from scrum.models import *


class ProfileForm(forms.ModelForm):
    AVA_OPTION = (
        ('YES', 'Yes'),
        ('NO', 'No')
    )

    availability = forms.ChoiceField(widget=forms.Select(attrs={'class':'form_input'}), choices=AVA_OPTION)


    class Meta:
        model = Profile
        fields = {'firstName', 'lastName', 'department', 'city', 'availability', 'phone','email'}
        widgets = {
            'firstName': forms.TextInput(attrs={'type': 'text','class':'form_input','placeholder':'Your First Name','data-rule':'minlen:4', 'data-msg':'Please enter at least 4 chars'}),
            'lastName': forms.TextInput(attrs={'type': 'text','class':'form_input',  'placeholder':'Your Last Name','data-rule':'minlen:4', 'data-msg':'Please enter at least 4 chars'}),
            'department': forms.TextInput(attrs={'type': 'text','class':'form_input', 'placeholder':'Your Department','data-rule':'minlen:4', 'data-msg':'Please enter at least 4 chars'}),
            'email': forms.EmailInput(attrs={'type': 'text','class':'form_input', 'placeholder':'Your Email','data-rule':'minlen:4', 'data-msg':'Please enter at least 4 chars'}),
            'phone': forms.TextInput(attrs={'type': 'text','class':'form_input', 'placeholder':'412-400-1234','data-rule':'minlen:4', 'data-msg':'Please enter at least 4 chars'}),
        }
