from django.urls import path, include
from apps.college.views import \
    StudentsViewset, CoursesViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunos', StudentsViewset, basename='Alunos')
router.register('cursos', CoursesViewset, basename='Cursos')

urlpatterns = [
    path('', include(router.urls) ),
]