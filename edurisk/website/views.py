from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, FormView, DetailView, View, UpdateView

posts = [
    {
        'author': 'EduRISK',
        'title' : ''
    },
]

def Home(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'website/home.html', context)

def Dashboard(request):
    context = {
        'title': 'Dashboard'
    }
    return render(request, 'website/dashboard.html', context)