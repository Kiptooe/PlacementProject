from django.db import models


class Applicant(models.Model):
    Id = models.BigAutoField(primary_key=True)
    First_Name = models.CharField(max_length=40)
    Second_Name = models.CharField(max_length=40)
    Last_Name = models.CharField(max_length=40)
    Email = models.EmailField()
    Phone = models.PositiveIntegerField()
    KCSE_Index = models.PositiveIntegerField()
    Year = models.PositiveIntegerField()
    Birth_Certificate_No = models.PositiveIntegerField()


class Institution(models.Model):
    Id = models.BigAutoField(primary_key=True)
    Institution_Name = models.TextField(max_length=200)
    Type_Id = models.ForeignKey("MinistryType", models.SET_NULL,
    blank=True, null=True)
    Ministry_Id = models.ForeignKey("Ministry", models.SET_NULL,
    blank=True, null=True)


class Ministry(models.Model):
    Id = models.BigAutoField(primary_key=True)
    Ministry_Name = models.TimeField(max_length=200)


class MinistryType(models.Model):
    Id = models.BigAutoField(primary_key=True)
    Type_Name = models.CharField(max_length=25)


class Course(models.Model):
    Id = models.BigAutoField(primary_key=True)
    Course_Name = models.CharField(max_length=200)
    Cluster_Id = models.ForeignKey("Cluster", models.SET_NULL, 
    blank=True, null=True)
    Institution_Id = models.ForeignKey("Institution", models.SET_NULL,
    null=True, blank=True)
    Course_Code = models.PositiveIntegerField()
    Cost = models.PositiveIntegerField()
    Capacity = models.PositiveIntegerField()


class Cluster(models.Model):
    Id = models.BigAutoField(primary_key=True)
    Cluster_Name = models.CharField(max_length=200)


class ClusterSubject(models.Model):
    Id = models.BigAutoField(primary_key=True)
    Cluster_Subject_Name = models.CharField(max_length=200)
    Cluster_Category_Id = models.ForeignKey("ClusterSubjectCategory", models.SET_NULL,
    blank=True, null=True )


class ClusterSubjectCategory(models.Model):
    Id = models.BigAutoField(primary_key=True)
    Cluster_Subject_Category_Name = models.CharField(max_length=200)


class Grade(models.Model):
    Id = models.BigAutoField(primary_key=True)
    Grade_Name = models.CharField(max_length=200)
    Grade_Value = models.PositiveIntegerField()


class Basket(models.Model):
    Id = models.BigAutoField(primary_key=True)
    Applicant_Id = models.ForeignKey("Applicant", models.SET_NULL,
    blank=True, null=True)

# class Application(models.Model):
#     Id = models.BigAutoField(primary_key=True)
#     Applicant_Id = models.ForeignKey("Applicant", models.SET_NULL,
#     null=True, blank=True)
#     First_Course_Id = models.ForeignKey("Course", models.SET_NULL,
#     blank=True, null=True)
#     Second_Course_Id = models.ForeignKey("Course", models.SET_NULL,
#     blank=True, null=True)
#     Third_Course_Id = models.ForeignKey("Course", models.SET_NULL, blank=True,
#     null=True)
#     Fourth_Course_Id = models.ForeignKey("Course", models.SET_NULL,
#     blank=True, null=True)
#     Fifth_Course_Id = models.ForeignKey("Course", models.SET_NULL,
#     blank=True, null=True)
#     Sixth_Course_Id = models.ForeignKey("Course", models.SET_NULL, blank=True,
#     null=True)
#     Payment_Id = models.ForeignKey("Payment", models.SET_NULL,
#     blank=True, null=True)

class Payment(models.Model):
    Id = models.BigAutoField(primary_key=True)
    Applicant_Id = models.ForeignKey("Applicant", models.SET_NULL,
    blank=True, null=True)
    Payment_Id = models.ForeignKey("Payment", models.SET_NULL,
    blank=True, null=True)


