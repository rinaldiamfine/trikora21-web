from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home, name='EvaLine-Home'),
    path('home', views.Home, name='EvaLine-Home'),
    path('dashboard', views.Dashboard, name='EvaLine-Dashboard'),
]