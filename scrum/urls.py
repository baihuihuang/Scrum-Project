from django.conf.urls import url
from scrum import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^create_profile$', views.create_profile, name='createProfile'),
    url(r'^create_manager$', views.create_manager, name='createManager'),
    url(r'^match_team$', views.match_team, name='matchTeam'),
]
