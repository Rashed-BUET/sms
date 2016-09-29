from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User



class Student(models.Model):
	user = models.OneToOneField(User, on_delete= models.CASCADE)

	date_of_birth = models.DateField()
	admission_year = models.IntegerField(default=2014)
	blood_group = models.CharField(default='A+', max_length=10)
	adress = models.CharField(default="Buet, Titumir Hall", max_length=200)
	profile_pic = models.ImageField(upload_to='school/images')


	def __str__(self):
		return self.user.username

class Teacher(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)


	join_date = models.DateField()
	designation = models.CharField( max_length=50)	
	blood_group = models.CharField(default='A+', max_length=10)
	address = models.CharField(default="BUET, Titumir Hall", max_length=200)
	profile_pic = models.ImageField()

class StudyMaterials(models.Model):


	name = models.CharField(max_length=100)
	file = models.FileField()
	extension = models.CharField( max_length=20)	

class Section(models.Model):



	room_no = models.CharField( max_length=50)
	total_student = models.IntegerField()
	capacity = models.IntegerField()


class AssignedSubject(models.Model):
	

	duration = models.IntegerField()
	class_per_week = models.IntegerField()


class ClubEvent(models.Model):
	

	event_type = models.CharField( max_length=200)
	date = models.DateField()
	details = models.TextField()

class ClubMember(models.Model):



	membership_status = models.CharField( max_length=100)

class Result(models.Model):


	marks = models.FloatField()
	grade = models.CharField(max_length=10)

class ClassTest(models.Model):



	date = models.DateField()
	marks = models.FloatField()
	syllabus = models.TextField()

class Subject(models.Model):



	subject_name = models.CharField( max_length=50)


class Club(models.Model):
		

		club_name = models.CharField( max_length=50)	
		office_room_no = models.CharField( max_length=50)
		total_members = models.IntegerField()



class Exam(models.Model):


	exam_name = models.CharField( max_length=50)
	exam_date = models.DateField()
	exam_routine = models.TextField()
	result_uploaded = models.IntegerField()
	sit_plan = models.TextField()


class Department(models.Model):


	dept_name = models.CharField( max_length=50)
	total_teachers = models.IntegerField()


class Notification(models.Model):



	not_type = models.CharField( max_length=50)
	hlink = models.CharField( max_length=200)
	details = models.TextField()
	date = models.DateField()
	view = models.BooleanField()
	


