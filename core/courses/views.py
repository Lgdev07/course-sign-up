from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from courses.models import Course
from courses.serializers import CourseSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from .tasks import sign_up_student


class CourseViewSet(viewsets.ModelViewSet):
  queryset = Course.objects.all()
  serializer_class = CourseSerializer

  @action(detail=False, methods=['post'])
  def signup(self, request, course_id):

    try:
      sign_up_student.delay(course_id)
    except Exception:
      return Response(status=status.HTTP_400_BAD_REQUEST)

    content = {'success': 'Send to the Sign Up Queue'}
    return Response(content, status=status.HTTP_201_CREATED)


