from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, CustomAuthenticationForm
from .models import Institution, InstitutionType, Applicant, MainResults, SubjectResults
from .functions import fetch_applicant_data

def index(request):
    
    private_count = Institution.objects.filter(Type_Id__Type_Name='Private').count()
    public_count = Institution.objects.filter(Type_Id__Type_Name='Public').count()

    context = {
        'private_count' : private_count,
        'public_count' : public_count
    }

    return render(request, 'home.html', context)

def applicant_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            user_dict = {
                'firstname':user.first_name,
                'secondname':user.last_name,
            }

            if user:
                login(request, user)

                fetch_applicant_data(sender=None, user=user, request=request)
                
                request.session['applicant_data'].update(user_dict)
            
                return redirect('dashboard')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form':form})

def applicant_logout(request):
    logout(request)
    return redirect('home')


def dashboard(request):
    applicant_data = request.session.get('applicant_data', {})
    
    subjects_data = SubjectResults.objects.filter(Applicant_Id=applicant_data['applicant_id'])
    average_results = MainResults.objects.get(Applicant_Id=applicant_data['applicant_id'])

    average_results = {
        'average_grade':average_results.Grade_Id.Grade_Name,
        'average_mark':average_results.Average,
        }
    
    for index, subject in enumerate(subjects_data, start=1):
        subjects_name_dict = {}
        subjects_results_dict = {}

        subjects_name_dict[f'Subject{index}'] = subject.Subject_Id.Cluster_Subject_Name
        subjects_results_dict[f'Result{index}'] = subject.Grade_Id.Grade_Name

        applicant_data.update(subjects_name_dict)
        applicant_data.update(subjects_results_dict)
        applicant_data.update(average_results)

    return render(request, 'dashboard.html', applicant_data)