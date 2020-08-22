from django.db import models

class Student(models.Model):
  name = models.CharField(max_length=255)
  
class Lecturer(models.Model):
  name = models.CharField(max_length=255)

class Course(models.Model):
  name = models.CharField(max_length=255)
  capacity = models.IntegerField()
  students = models.ManyToManyField(Student, null=True)
  lecturer = models.ForeignKey(Lecturer, on_delete=models.RESTRICT, null=True)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now_add=True)


