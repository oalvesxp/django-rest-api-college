from rest_framework import serializers
from apps.college.models import \
    Student, Course, Enrolment

class StudentSrializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'id',
            'name',
            'cpf',
            'birth'
        ]

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class EnrolmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrolment
        exclude = []
