from rest_framework import viewsets, generics
from apps.college.models import \
    Student, Course, Enrolment
from apps.college.serializer import \
    StudentSrializer, CourseSerializer, EnrolmentSerializer, StudentEnrolmentListSerializer, CourseStudentListSerializer

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

class StudentEnrolmentList(generics.ListAPIView):
    '''Exibindo todas as matrículas de um aluno específico'''
    def get_queryset(self):
        queryset = Enrolment.objects.filter(student_id=self.kwargs['pk'])
        return queryset
    serializer_class = StudentEnrolmentListSerializer

class CourseStudentList(generics.ListAPIView):
    '''Exibindo alunos matrículados em um determinado curso'''
    def get_queryset(self):
        queryset = Enrolment.objects.filter(course_id=self.kwargs['pk'])
        return queryset
    serializer_class = CourseStudentListSerializer