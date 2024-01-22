from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('memberships/', views.memberships, name='memberships'),
    path('classes/', views.classes, name='classes'),
    path('contact/', views.contact, name='contact'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('classes/booking', views.booking, name='booking'),
]