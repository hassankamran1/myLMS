# Generated by Django 4.2.6 on 2023-10-29 23:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student_records', '0001_initial'),
        ('course_info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrollment_date', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_info.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_records.student')),
            ],
            options={
                'unique_together': {('student', 'course')},
            },
        ),
    ]