from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('logout/', views.applicant_logout, name='logout'),    
    path('login/', views.applicant_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('application/', views.application, name='application'),
    path('apply/', views.apply, name='apply'),
    path('fetch_course_details/', views.fetch_course_details, name='course_details')
]
