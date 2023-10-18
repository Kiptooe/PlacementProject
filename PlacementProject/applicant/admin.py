from django.contrib import admin
from .models import Applicant, MinistryType, Ministry


admin.site.register(Applicant)
admin.site.register(Ministry)
admin.site.register(MinistryType)