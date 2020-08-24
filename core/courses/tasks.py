import string
from django.shortcuts import render, get_object_or_404
from django.core.exceptions import ValidationError
from courses.models import Course
from celery import shared_task

@shared_task
def sign_up_student(course_id):
    course = get_object_or_404(Course, pk=course_id)

    if course.students == course.capacity:
        return ValidationError("The Course is Full")

    course.students += 1
    course.save()
