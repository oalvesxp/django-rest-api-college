from django.urls import path
from apps.college.views import \
    students

urlpatterns = [
    path('alunos/', students),
]