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

class StudentEnrolmentListSerializer(serializers.ModelSerializer):
    course = serializers.ReadOnlyField(source='course.description')
    period = serializers.SerializerMethodField()
    class Meta:
        model = Enrolment
        fields = ['course', 'period']

    def get_period(self, object):
        return object.get_period_display()