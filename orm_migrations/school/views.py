from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    context = {}
    persons = Student.objects.order_by('name').prefetch_related('teachers')
    return render(request, template, {'object_list': persons})

#    Без prefetch_related:
# http://127.0.0.1:8000/  6 запросов к БД

#    C prefetch_related:
# http://127.0.0.1:8000/  4 запроса к БД
