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
            'firstName': forms.TextInput(attrs={'type': 'text','class':'form_input','placeholder':'Your First Name','data-rule':'minlen:4', 'data-msg':'Please enter at least 4 chars', 'required':'True'}),
            'lastName': forms.TextInput(attrs={'type': 'text','class':'form_input',  'placeholder':'Your Last Name','data-rule':'minlen:4', 'data-msg':'Please enter at least 4 chars', 'required':'True'}),
            'department': forms.TextInput(attrs={'type': 'text','class':'form_input', 'placeholder':'Your Department','data-rule':'minlen:4', 'data-msg':'Please enter at least 4 chars', 'required':'True'}),
            'email': forms.EmailInput(attrs={'type': 'text','class':'form_input', 'placeholder':'Your Email','data-rule':'minlen:4', 'data-msg':'Please enter at least 4 chars', 'required':'True'}),
            'phone': forms.TextInput(attrs={'type': 'text','class':'form_input', 'placeholder':'412-400-1234','data-rule':'minlen:4', 'data-msg':'Please enter at least 4 chars', 'required':'True'}),
        }


class SkillForm(forms.ModelForm):
    PRO_LEVEL = (
        ('null', 'Please Choose'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )

    SKILLS = (
        ('null', 'Please Choose'),
        ('Java', 'Java'),
        ('Python', 'Python'),
        ('C', 'C'),
        ('C++', 'C++'),
        ('C#', 'C#'),
        ('SQL', 'SQL'),
        ('MySQL', 'MySQL'),
        ('MongoDB', 'MongoDB'),
        ('Marketing', 'Marketing'),
        ('Analytics', 'Analytics'),
        ('Web Development', 'Web Development'),
        ('Design', 'Design'),
        ('Agile', 'Agile')
    )
    proficiency = forms.ChoiceField(widget=forms.Select(attrs={'class':'form_input'}), choices=PRO_LEVEL)
    name = forms.ChoiceField(widget=forms.Select(attrs={'class':'form_input'}), choices=SKILLS)

    class Meta:
        model = Skill
        fields = {'name', 'yrOfExperience'}
        widgets = {
            'yrOfExperience': forms.NumberInput(attrs={'class':'form_input', 'placeholder':'4 (years)','data-rule':'minlen:4', 'data-msg':'Please enter at least 4 chars', 'required':'True'}),
        }


class ManagerForm(forms.ModelForm):
    TEAM_CHOICE = (
        ('null', 'Please Choose'),
        ('1', '1'),
        ('2', '2'),
    )
    TEAM_PEOPLE_CHOICE = (
        ('null', 'Please Choose'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
    )
    numberOfTeam = forms.ChoiceField(widget=forms.Select(attrs={'class':'form_input', 'onchange': 'myFunction()', 'id':'team-num'}), choices=TEAM_CHOICE)
    numberPPlOfTeam = forms.ChoiceField(widget=forms.Select(attrs={'class':'form_input'}), choices=TEAM_PEOPLE_CHOICE)

    class Meta:
        model = Manager
        fields = {'numberOfTeam', 'numberPPlOfTeam'}


class MinSkillForm(forms.ModelForm):
    PRO_LEVEL = (
        ('null', 'Please Choose'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )

    SKILLS = (
        ('null', 'Please Choose'),
        ('Java', 'Java'),
        ('Python', 'Python'),
        ('C', 'C'),
        ('C++', 'C++'),
        ('C#', 'C#'),
        ('SQL', 'SQL'),
        ('MySQL', 'MySQL'),
        ('MongoDB', 'MongoDB'),
        ('Marketing', 'Marketing'),
        ('Analytics', 'Analytics'),
        ('Web Development', 'Web Development'),
        ('Design', 'Design'),
        ('Agile', 'Agile')
    )
    proficiency = forms.ChoiceField(widget=forms.Select(attrs={'class':'form_input'}), choices=PRO_LEVEL)
    name = forms.ChoiceField(widget=forms.Select(attrs={'class':'form_input'}), choices=SKILLS)

    class Meta:
        model = MinSkill
        fields = {'name', 'yrOfExperience'}
        widgets = {
            'yrOfExperience': forms.NumberInput(attrs={'class':'form_input', 'placeholder':'4 (years)','data-rule':'minlen:4', 'data-msg':'Please enter at least 4 chars', 'required':'True'}),
        }
