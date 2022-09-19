from django.contrib import admin

from .models import Student, Teacher


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'group', 'id')


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject')
