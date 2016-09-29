from django.forms import ModelForm 
from .models import Student, Teacher
from django.contrib.auth.models import User
from django import forms
from django.contrib.admin import widgets 
from functools import partial
DateInput = partial(forms.DateInput, {'class': 'datepicker'})


class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		exclude = []
		widgets = {
		            'date_of_birth': DateInput(),
		            'user': forms.HiddenInput(),
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





class StudentLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)







