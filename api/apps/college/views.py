from rest_framework import viewsets
from apps.college.models import \
    Student, Course, Enrolment
from apps.college.serializer import \
    StudentSrializer, CourseSerializer, EnrolmentSerializer

class StudentsViewset(viewsets.ModelViewSet):
    '''Exibindo todos os alunos e alunas'''
    queryset = Student.objects.all()
    serializer_class = StudentSrializer

class CoursesViewset(viewsets.ModelViewSet):
    '''Exibindo todos os cursos'''
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class EnrolmentViewset(viewsets.ModelViewSet):
    '''Exibindo todas as matrículas'''
    queryset = Enrolment.objects.all()
    serializer_class = EnrolmentSerializer