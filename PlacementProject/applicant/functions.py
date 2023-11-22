from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from .models import Applicant, MainResults, SubjectResults, User
from django.contrib.auth.hashers import make_password
from django.db.models.signals import pre_save


@receiver(pre_save, sender=User)
def hash_user_password(sender, instance, **kwargs):
    if instance._state.adding:  # Check if it's a new user being added
        instance.password = make_password(instance.password)


@receiver(user_logged_in)
def fetch_applicant_data(sender, request, user, **kwargs):

    if user.is_authenticated:

        user_id = user.id

        try:

            applicant_data = Applicant.objects.get(User_Id=user_id)

            high_school_name = applicant_data.HighSchool_Id.Name if applicant_data.HighSchool_Id else None

            request.session['applicant_data'] = {
                'applicant_id':applicant_data.Id,
                'email':applicant_data.Email,
                'phone':applicant_data.Phone,
                'year':applicant_data.Year,
                'gender':applicant_data.Gender,
                'citizenship':applicant_data.Citizenship,
                'highschool':high_school_name,
                'index':applicant_data.KCSE_Index,
            }
        except Applicant.DoesNotExist:
            pass

    