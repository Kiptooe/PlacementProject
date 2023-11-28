from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Application

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs)
        
        # Adding form-control class to the username and password fields
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})

class CourseForm(forms.Form):
    first_course_code = forms.CharField(max_length=100)
    second_course_code = forms.CharField(max_length=100)
    third_course_code = forms.CharField(max_length=100)
    fourth_course_code = forms.CharField(max_length=100)
    fifth_course_code = forms.CharField(max_length=100)
    sixth_course_code = forms.CharField(max_length=100)