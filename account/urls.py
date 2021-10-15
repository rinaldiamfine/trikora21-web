from django.urls import path, include
from . import views

urlpatterns = [
    path('myprofile', views.myProfile, name='edurisk-myprofile'),
    path('profile/<int:profile_id>', views.profileForm, name='edurisk-profile'),
    path('profile', views.profileList, name='edurisk-profile'),
]