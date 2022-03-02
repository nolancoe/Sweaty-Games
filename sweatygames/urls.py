from django.urls import path
from .views import MatchView, MatchDetailView, CreateMatchView, CreateTeamView
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('matches/', MatchView.as_view(), name="matches"),
    path('match/<int:pk>', MatchDetailView.as_view(), name='match-detail'),
    path('create_match/', CreateMatchView.as_view(), name='create_match'),
    path('create_team/', CreateTeamView.as_view(), name='create_team'),

]


