from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('logout/', views.applicant_logout, name='logout'),    
    path('login/', views.applicant_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard')
]