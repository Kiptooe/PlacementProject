# Generated by Django 4.2.5 on 2023-11-02 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applicant', '0006_rename_cost_course_year_1_course_cost'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MinistryType',
            new_name='InstitutionType',
        ),
    ]
