from django.forms import ModelForm 
from .models import Student, Teacher
from django.contrib.auth.models import User
from django import forms
from django.contrib.admin import widgets 



class StudentForm(ModelForm):
	class Meta:
		model = Student
		exclude = ['user']
		widgets = {
		            'date_of_birth': widgets.AdminDateWidget(),
		        }


class TeacherForm(ModelForm):
	class Meta:
		model = Teacher
		exclude = []		


class UserForm(ModelForm):
	class Meta:
		model = User
		fields = ['username','password','email','first_name','last_name']				
		widgets = {
		            'password': forms.PasswordInput(),
		        }













