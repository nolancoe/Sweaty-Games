from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView, DetailView, CreateView
from .models import Match, Team

def home(request):
    return render(request, 'home.html', {})

class MatchView(ListView):
    model = Match
    template_name = 'matches.html'

class MatchDetailView(DetailView):
    model = Match
    template_name = 'match_details.html'

class CreateMatchView(CreateView):
    model = Match
    template_name = 'create_match.html'
    fields = '__all__'

class CreateTeamView(CreateView):
    model = Team
    template_name = 'create_team.html'
    fields = '__all__'
