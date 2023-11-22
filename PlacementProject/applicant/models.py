from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class User(AbstractUser):
    is_applicant = models.BooleanField(default=False)
    
    groups = models.ManyToManyField(Group, related_name='placeholder_user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='placeholder_user_permissions')


class Applicant(models.Model):

    GENDER_CHOICES = [
        ('M', "Male"),
        ('F', "Female"),
    ]

    CITIZENSHIP_STATUS = [
        ('C', "Citizen"),
        ('NC', "Not Citizen"),
    ]
    Id = models.BigAutoField(primary_key=True)
    Email = models.EmailField()
    Phone = models.PositiveIntegerField()
    KCSE_Index = models.PositiveIntegerField()
    Year = models.PositiveIntegerField()
    Gender = models.CharField(choices=GENDER_CHOICES, max_length=15)
    Citizenship = models.CharField(choices=CITIZENSHIP_STATUS, max_length=15)
    HighSchool_Id = models.ForeignKey("HighSchool", on_delete=models.CASCADE,
    blank=True, null=True)
    Birth_Certificate_No = models.PositiveIntegerField()
    User_Id = models.ForeignKey("User", on_delete=models.CASCADE,
    null=True, blank=True)

    def __str__(self):
        return f"{self.User_Id}"  


class HighSchool(models.Model):
    Id = models.BigAutoField(primary_key=True)
    Name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.Name}"


class Institution(models.Model):
    Id = models.BigAutoField(primary_key=True)
    Institution_Name = models.TextField(max_length=200)
    Type_Id = models.ForeignKey("InstitutionType",on_delete= models.CASCADE,
    blank=True, null=True)
    Ministry_Id = models.ForeignKey("Ministry", on_delete=models.CASCADE,
    blank=True, null=True)

    def __str__(self):
        return f"{self.Institution_Name}"

class Ministry(models.Model):
    Id = models.BigAutoField(primary_key=True)
    Ministry_Name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.Ministry_Name}"


class InstitutionType(models.Model):
    Id = models.BigAutoField(primary_key=True)
    Type_Name = models.CharField(max_length=25)

    def __str__(self) -> str:
        return f"{self.Type_Name}"

class Course(models.Model):
    Id = models.BigAutoField(primary_key=True)
    Course_Name = models.CharField(max_length=200)
    Cluster_Id = models.ForeignKey("Cluster", on_delete=models.CASCADE, 
    blank=True, null=True)
    Institution_Id = models.ForeignKey("Institution", on_delete=models.CASCADE,
    blank=True, null=True)
    Course_Code = models.PositiveIntegerField()
    Year_1_Course_Cost = models.PositiveIntegerField()
    Capacity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.Course_Name}"


class Cluster(models.Model):
    Id = models.BigAutoField(primary_key=True)
    Cluster_Name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.Cluster_Name}"

class Subject(models.Model):
    Id = models.BigAutoField(primary_key=True)
    Cluster_Subject_Name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.Cluster_Subject_Name}"

class SubjectCategory(models.Model):
    Id = models.BigAutoField(primary_key=True)
    Subject_Id = models.ForeignKey("Subject", on_delete=models.CASCADE,
    blank=True, null=True)
    Category_Id = models.ForeignKey("ClusterSubjectCategory", on_delete=models.CASCADE,
    null=True, blank=True)
    Cluster_Id = models.ForeignKey("Cluster", on_delete=models.CASCADE,
    blank=True, null=True)


class ClusterSubjectCategory(models.Model):
    Id = models.BigAutoField(primary_key=True)
    Cluster_Subject_Category_Name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.Cluster_Subject_Category_Name}"

class Grade(models.Model):
    Id = models.BigAutoField(primary_key=True)
    Grade_Name = models.CharField(max_length=200)
    Grade_Value = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.Grade_Name}"


class Basket(models.Model):
    Id = models.BigAutoField(primary_key=True)
    Applicant_Id = models.ForeignKey("Applicant",on_delete=models.CASCADE,
    blank=True, null=True)
    Course_Id = models.ForeignKey("Course", on_delete=models.CASCADE,
    blank=True, null=True)

class SubjectMinCategory(models.Model):
    Id = models.BigAutoField(primary_key=True)
    Course_Id = models.ForeignKey("Course", on_delete=models.CASCADE, blank=True, null=True )
    Subject_Id = models.ForeignKey("Subject", on_delete=models.CASCADE, blank=True, null=True)
    Category_Id = models.ForeignKey("MinSubjectCategory", on_delete=models.CASCADE,
    null=True, blank=True)
    Grade_Id = models.ForeignKey("Grade", on_delete=models.CASCADE,
    null=True, blank=True)


class MinSubjectCategory(models.Model):
    Id = models.BigAutoField(primary_key=True)
    Minimum_Subject_Category_Name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.Minimum_Subject_Category_Name}"

class Payment(models.Model):
    Id = models.BigAutoField(primary_key=True)
    Applicant_Id = models.ForeignKey("Applicant", on_delete=models.CASCADE,
    blank=True, null=True)
    Payment_Code = models.CharField(max_length=100)


class MainResults(models.Model):
    Id = models.BigAutoField(primary_key=True)
    Grade_Id = models.ForeignKey("Grade", on_delete=models.CASCADE, blank=True, null=True)
    Average = models.IntegerField()
    Applicant_Id = models.ForeignKey("Applicant", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.Grade_Id}"


class SubjectResults(models.Model):
    Id = models.BigAutoField(primary_key=True)
    Applicant_Id = models.ForeignKey("Applicant", on_delete=models.CASCADE, blank=True, null=True)
    Subject_Id = models.ForeignKey("Subject", on_delete=models.CASCADE, blank=True, null=True)
    Grade_Id = models.ForeignKey("Grade", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.Grade_Id}"


class Application(models.Model):

    COURSE_RANKS = [
        (1, "1(a)"),
        (2, "1(b)"),
        (3, "1(c)"),
        (4, "2"),
        (5, "3"),
        (6, "4"),
    ]

    Id = models.BigAutoField(primary_key=True)
    Applicant_Id = models.ForeignKey("Applicant", on_delete=models.CASCADE, blank=True, null=True)
    Course_Id = models.ForeignKey("Course", on_delete=models.CASCADE, blank=True, null=True)
    Course_Rank = models.CharField(max_length=1, choices=COURSE_RANKS)
    Payment_Id = models.ForeignKey("Payment", on_delete=models.CASCADE,
    blank=True, null=True)




