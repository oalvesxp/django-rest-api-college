from rest_framework import serializers
from apps.college.models import \
    Student, Course

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
