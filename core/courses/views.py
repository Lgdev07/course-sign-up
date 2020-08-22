from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from courses.models import Course, Student
from courses.serializers import CourseSerializer, StudentSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class CourseViewSet(viewsets.ModelViewSet):
  queryset = Course.objects.all()
  serializer_class = CourseSerializer

  @action(detail=False, methods=['post'])
  def signup(self, request, course_id, student_id):
    course = Course.objects.filter(pk=course_id, students=student_id)
    
    if course:
      content = {'error': 'The Student is Already Enrolled In this Course'}
      return Response(content, status=status.HTTP_404_NOT_FOUND)

    course = get_object_or_404(Course, pk=course_id)
    student = get_object_or_404(Student, pk=student_id)    

    course.students.add(student)
    course.save()
    return Response(status=status.HTTP_201_CREATED)

class StudentViewSet(viewsets.ModelViewSet):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer


