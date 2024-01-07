from rest_framework import viewsets, generics
from apps.college.models import \
    Student, Course, Enrolment
from apps.college.serializer import \
    StudentSrializer, CourseSerializer, EnrolmentSerializer, StudentEnrolmentListSerializer, CourseStudentListSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class StudentsViewset(viewsets.ModelViewSet):
    '''Exibindo todos os alunos e alunas'''
    queryset = Student.objects.all()
    serializer_class = StudentSrializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class CoursesViewset(viewsets.ModelViewSet):
    '''Exibindo todos os cursos'''
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class EnrolmentViewset(viewsets.ModelViewSet):
    '''Exibindo todas as matrículas'''
    queryset = Enrolment.objects.all()
    serializer_class = EnrolmentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class StudentEnrolmentList(generics.ListAPIView):
    '''Exibindo todas as matrículas de um aluno específico'''
    def get_queryset(self):
        queryset = Enrolment.objects.filter(student_id=self.kwargs['pk'])
        return queryset
    serializer_class = StudentEnrolmentListSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class CourseStudentList(generics.ListAPIView):
    '''Exibindo alunos matrículados em um determinado curso'''
    def get_queryset(self):
        queryset = Enrolment.objects.filter(course_id=self.kwargs['pk'])
        return queryset
    serializer_class = CourseStudentListSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]