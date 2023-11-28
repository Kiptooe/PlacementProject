from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, CustomAuthenticationForm, CourseForm
from .models import Institution, InstitutionType, Applicant, MainResults, SubjectResults, Course, Application
from .functions import fetch_applicant_data, is_ajax
from django.http import JsonResponse

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

def application(request):
    applicant_id = request.session['applicant_data'].get('applicant_id')
    applications = Application.objects.filter(Applicant_Id=applicant_id)
    
    applied = applications.exists()
        
    return render(request, 'application.html', {'status': applied})

def apply(request):

    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            applicant_id = request.session['applicant_data'].get('applicant_id')

            applicant = Applicant.objects.get(pk=applicant_id)

            course_codes = [
                form.cleaned_data['first_course_code'],
                form.cleaned_data['second_course_code'],
                form.cleaned_data['third_course_code'],
                form.cleaned_data['fourth_course_code'],
                form.cleaned_data['fifth_course_code'],
                form.cleaned_data['sixth_course_code'],
            ]

            valid_courses = Course.objects.filter(Course_Code__in=course_codes)
            for rank, code in enumerate(course_codes, start=1):
                try:
                    course = valid_courses.get(Course_Code=code)
                    course_object = Course.objects.get(pk=course.Id)        


                    Application.objects.create(
                        Applicant_Id=applicant,
                        Course_Id=course_object,
                        Course_Rank=rank
                    )
                except Course.DoesNotExist:
                    print('Course Does not exist')
            
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        course_form = CourseForm()

    return render(request, 'apply.html', {'course_form': course_form})


def fetch_course_details(request):
    if is_ajax(request) and request.method == 'GET':
        course_code = request.GET.get('course_code')
        try:
            course = Course.objects.get(Course_Code=course_code)
            data = {
                'course_name': course.Course_Name,
                'institution_name': course.Institution_Id.Institution_Name
            }
        except Course.DoesNotExist:
            print(course_code)
            data = {'error':'Invalid code'}

        return JsonResponse(data)
    
    return JsonResponse({'error': 'Invalid request'})

