from django.contrib import admin
from .models import *
from django.urls import reverse
from django.utils.html import format_html
# from django_otp.admin import OTPAdminSite
# from django.contrib.auth.models import User, Group
# from django_otp.plugins.otp_totp.models import TOTPDevice
# from django_otp.plugins.otp_totp.admin import TOTPDeviceAdmin



# class OTPAdmin(OTPAdminSite):
#     pass


# admin_site = OTPAdmin(name='OTPAdmin')
# admin_site.register(User)
# admin_site.register(Group)
# admin_site.register(TOTPDevice, TOTPDeviceAdmin)
# admin_site.register(Applicant)
# admin_site.register(MinistryType)
# admin_site.register(Ministry)
# admin_site.register(Institution)
# admin_site.register(Course)
# admin_site.register(Cluster)
# admin_site.register(ClusterSubject)
# admin_site.register(ClusterSubjectCategory)
# admin_site.register(Grade)
# admin_site.register(Application)
# admin_site.register(Basket)
# admin_site.register(Payment)
# admin_site.register(SubjectResults)
# admin_site.register(MainResults)
# admin_site.register(ClusterCategory)
# admin_site.register(ClusterMinGrade)
# admin_site.register(ClusterMinSubject)

class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'is_applicant']

class ApplicantAdmin(admin.ModelAdmin):

    def get_gender_distribution_link(self, obj):
        
        url = reverse('applicant:gender_distribution')
        return format_html(' <a href="{}"> View Gender Distribution </a>', url)
    

    get_gender_distribution_link.short_description = 'Gender Distribution'

    list_display = ['Email', 'Phone', 'KCSE_Index', 'Year', 'get_gender_distribution_link']

class InstitutionAdmin(admin.ModelAdmin):
   
    def get_top_institution_distribution_link(self, obj):
        url = reverse('applicant:top-institution-distribution')
        return format_html(' <a href="{}"> View Institution Distribution </a>', url)
    

    get_top_institution_distribution_link.short_description = 'Top Institution Distribution'

    list_display = ['Institution_Name', 'Type_Id', 'Ministry_Id', 'get_top_institution_distribution_link']


class MinistryAdmin(admin.ModelAdmin):
    list_display = ['Ministry_Name']

class InstitutionTypeAdmin(admin.ModelAdmin):
    
    def get_institutions_distribution_link(self, obj):
        url = reverse('applicant:institutions_distribution')
        return format_html(' <a href="{}"> View Institutions Distribution by applicant </a>', url)
    

    get_institutions_distribution_link.short_description = 'Institutions Distribution by Applicants'


    def get_institution_distribution_link(self, obj):
        url = reverse('applicant:institution_distribution')
        return format_html(' <a href="{}"> View Institution Distribution </a>', url)
    

    get_institution_distribution_link.short_description = 'Institution Distribution'

    list_display = ['Type_Name', 'get_institutions_distribution_link', 'get_institution_distribution_link']

class CourseAdmin(admin.ModelAdmin):

    def get_course_distribution_link(self, obj):
        url = reverse('applicant:course_distribution')
        return format_html(' <a href="{}"> View Course Distribution </a>', url)
    
    get_course_distribution_link.short_description = 'Course Distribution'

    list_display = ['Course_Name', 'Cluster_Id', 'Institution_Id', 'Course_Code', 'Year_1_Course_Cost', 'Capacity', 'get_course_distribution_link']

class ClusterAdmin(admin.ModelAdmin):
    list_display = ['Cluster_Name']

class SubjectAdmin(admin.ModelAdmin):
    list_display = ['Cluster_Subject_Name']

class SubjectCategoryAdmin(admin.ModelAdmin):
    list_display = ['Cluster_Id', 'Category_Id', 'Subject_Id']

class ClusterSubjectCategoryAdmin(admin.ModelAdmin):
    list_display = ['Cluster_Subject_Category_Name']

class GradeAdmin(admin.ModelAdmin):
    list_display = ['Grade_Name', 'Grade_Value']

class BasketAdmin(admin.ModelAdmin):
    list_display = ['Applicant_Id', 'Course_Id']

class SubjectMinCategoryAdmin(admin.ModelAdmin):
    list_display = ['Category_Id', 'Subject_Id', 'Grade_Id']

class MinSubjectCategoryAdmin(admin.ModelAdmin):
    list_display = ['Minimum_Subject_Category_Name']

class PaymentAdmin(admin.ModelAdmin):
    list_display = ['Applicant_Id']

class MainResultsAdmin(admin.ModelAdmin):
    list_display = ['Applicant_Id', 'Grade_Id', 'Average']

class SubjectResultsAdmin(admin.ModelAdmin):
    list_display = ['Applicant_Id', 'Subject_Id', 'Grade_Id']

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['Applicant_Id', 'Course_Id', 'Course_Rank']

class HighSchoolAdmin(admin.ModelAdmin):
    list_display = ['Name']

admin.site.register(InstitutionType, InstitutionTypeAdmin)
admin.site.register(Ministry, MinistryAdmin)
admin.site.register(Institution, InstitutionAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Cluster, ClusterAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(ClusterSubjectCategory, ClusterSubjectCategoryAdmin)
admin.site.register(Grade, GradeAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(Basket, BasketAdmin)
# admin.site.register(Payment, PaymentAdmin)
admin.site.register(SubjectResults, SubjectResultsAdmin)
admin.site.register(MainResults, MainResultsAdmin)
admin.site.register(SubjectMinCategory, SubjectMinCategoryAdmin)
admin.site.register(MinSubjectCategory, MinSubjectCategoryAdmin)
admin.site.register(SubjectCategory, SubjectCategoryAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Applicant, ApplicantAdmin)
admin.site.register(HighSchool, HighSchoolAdmin)


