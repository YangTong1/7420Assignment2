
# Create your models here.
from django.db import models

#USER => 系统的用户 它可以是老师 也可以是学生
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=50)

class Lecturer(models.Model):
    staff_id = models.IntegerField()
    DOB = models.DateTimeField()
    user = models.OneToOneField(User, on_delete=models.SET_NULL,null=True)

class Semester(models.Model):
    id = models.AutoField(primary_key=True)
    year = models.IntegerField()
    semester = models.CharField(max_length=50)
    course = models.ManyToManyField("Course")



class Course(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

class Class(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.IntegerField()
    course = models.ForeignKey("Course", on_delete=models.SET_NULL,null=True)
    semester = models.ForeignKey("Semester",on_delete=models.SET_NULL,null=True)
    lecturer = models.ForeignKey("Lecturer",on_delete=models.SET_NULL,null=True)
    # student = models.ManyToManyField("Student", related_name="student")

class Student(models.Model):
    student_id = models.IntegerField()
    DOB = models.DateTimeField()
    user = models.OneToOneField(User, on_delete=models.SET_NULL,null=True)
    attend = models.FloatField()
    # myclass = models.ForeignKey("Class",on_delete=models.SET_NULL,null=True)
    mycourse = models.ManyToManyField("Course")
    myclass = models.ManyToManyField("Class",related_name="myclass")

class College_Day(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    myclass = models.ManyToManyField(Class)
    student = models.ManyToManyField(Student)