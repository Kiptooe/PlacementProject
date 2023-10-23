from django.contrib import admin
from .models import Applicant, MinistryType, Ministry, Institution, Course, Cluster, ClusterSubject, ClusterSubjectCategory, Grade, Basket, Payment
from django_otp.admin import OTPAdminSite
from django.contrib.auth.models import User
from django_otp.plugins.otp_totp.models import TOTPDevice
from django_otp.plugins.otp_totp.admin import TOTPDeviceAdmin


class OTPAdmin(OTPAdminSite):
    pass


admin_site = OTPAdmin(name='OTPAdmin')
admin_site.register(User)
admin_site.register(TOTPDevice, TOTPDeviceAdmin)
admin_site.register(Applicant)
admin_site.register(MinistryType)
admin_site.register(Ministry)
admin_site.register(Institution)
admin_site.register(Course)
admin_site.register(Cluster)
admin_site.register(ClusterSubject)
admin_site.register(ClusterSubjectCategory)
admin_site.register(Grade)
# admin_site.register(Application)
admin_site.register(Basket)
admin_site.register(Payment)


# admin.site.register(Applicant)
# admin.site.register(Ministry)
# admin.site.register(MinistryType)