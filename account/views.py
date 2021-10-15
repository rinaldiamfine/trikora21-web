from django.shortcuts import render, redirect

# Create your views here.
# from django.contrib.auth.models import User
# from .models import User
from django.contrib.auth import get_user_model, logout
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, FormView, DetailView, View, UpdateView
User = get_user_model()

from edurisk.mixins import NextUrlMixin, RequestFormAttachMixin
from .models import *
from .forms import LoginForm, ProfileForm

version = '2020.1.1'
def myProfile(request):
    active_user = request.user
    profile_id = Profile.objects.get(profile_user=active_user.id)
    form = ProfileForm(instance=profile_id, initial={})
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile_id)
        if form.is_valid():
            profile_id = form.save(commit=False)
            profile_id.save()
            return redirect('/myprofile')
    context = {'title': 'My Profile', 'form': form, 'version': version}
    return render(request, 'account/profile.html', context)

def profileForm(request, profile_id):
    profile_id = Profile.objects.get(pk=profile_id)
    form = ProfileForm(instance=profile_id, initial={})
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile_id)
        if form.is_valid():
            profile_id = form.save(commit=False)
            profile_id.save()
            return redirect('/profile/'+ str(profile_id.id))
    context = {'title': 'Profile', 'form': form, 'version': version}
    return render(request, 'account/profile.html', context)

def profileList(request):
    profile_ids = Profile.objects.all()
    context = {'title': 'Profiles', 'list': profile_ids, 'version': version}
    return render(request, 'account/profiles.html', context)

class LoginView(NextUrlMixin, RequestFormAttachMixin, FormView):
    form_class = LoginForm
    success_url = '/'
    template_name = 'account/login.html'
    default_next = '/dashboard'

    def form_valid(self, form):
        next_path = self.get_next_url()
        return redirect(next_path)

def signout(request):
    if request.method == "POST":
        logout(request)
        return redirect('/')