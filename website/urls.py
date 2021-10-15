from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home, name='EduRISK-Home'),
    path('home', views.Home, name='EduRISK-Home'),
    path('dashboard', views.Dashboard, name='EduRISK-Dashboard'),
]