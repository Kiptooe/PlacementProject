# Generated by Django 4.2.5 on 2023-10-18 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('applicant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('inst_name', models.TextField(max_length=200)),
                ('ministry_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='applicant.ministrytype')),
                ('type_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='applicant.ministry')),
            ],
        ),
    ]