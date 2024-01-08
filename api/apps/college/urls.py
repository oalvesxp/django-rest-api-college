from django.urls import path, include
from apps.college.views import \
    StudentsViewset, CoursesViewset, EnrolmentViewset, StudentEnrolmentList, CourseStudentList
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunos', StudentsViewset, basename='Alunos')
router.register('cursos', CoursesViewset, basename='Cursos')
router.register('matriculas', EnrolmentViewset, basename='Matriculas')

urlpatterns = [
    path('', include(router.urls) ),
    path('aluno/<int:pk>/matriculas/', StudentEnrolmentList.as_view()),
    path('curso/<int:pk>/matriculas/', CourseStudentList.as_view()),
]