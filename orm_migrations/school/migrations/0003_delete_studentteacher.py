# Generated by Django 4.1.1 on 2022-09-17 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_alter_student_options_remove_student_teacher_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StudentTeacher',
        ),
    ]
