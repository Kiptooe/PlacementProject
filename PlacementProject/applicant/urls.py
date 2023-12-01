from django.urls import path
from . import views

app_name = 'applicant'
urlpatterns = [
    path('', views.index, name = 'home'),
    path('logout/', views.applicant_logout, name='logout'),    
    path('login/', views.applicant_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('application/', views.application, name='application'),
    path('apply/', views.apply, name='apply'),
    path('fetch_course_details/', views.fetch_course_details, name='course_details'),
    path('institution-distribution/', views.institution_distribution_view, name='institution_distribution'),
    path('gender-distribution/', views.gender_distribution_view, name='gender_distribution'),
    path('top-institution-distribution/', views.top_institution_view, name='top-institution-distribution'),
    path('course_distribution/', views.course_distribution_view, name='course_distribution'),
    path('institutions_distribution/', views.institutions_distribution_view, name='institutions_distribution')

]
