from rest_framework import serializers
from courses.models import Course, Student

class CourseSerializer(serializers.ModelSerializer):
  class Meta:
    model = Course
    fields = ['name', 'capacity']

class StudentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Student
    fields = ['name']
