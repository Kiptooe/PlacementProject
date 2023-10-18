from django.db import models


class Applicant(models.Model):
    Id = models.BigAutoField(primary_key=True)
    f_name = models.CharField(max_length=40)
    s_name = models.CharField(max_length=40)
    l_name = models.CharField(max_length=40)
    email = models.EmailField()
    phone = models.PositiveIntegerField()
    kcse_index = models.PositiveIntegerField()
    year = models.PositiveIntegerField()
    birth_cert_no = models.PositiveIntegerField()


class Institution(models.Model):
    id = models.BigAutoField(primary_key=True)
    inst_name = models.TextField(max_length=200)
    type_id = models.ForeignKey("Ministry", models.SET_NULL,
    blank=True, null=True)
    ministry_id = models.ForeignKey("MinistryType", models.SET_NULL,
    blank=True, null=True)


class Ministry(models.Model):
    id = models.BigAutoField(primary_key=True)
    min_name = models.TimeField(max_length=200)


class MinistryType(models.Model):
    id = models.BigAutoField(primary_key=True)
    type_name = models.CharField(max_length=25)



