from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^studentsignup/$', views.student_signup, name = 'st_signup'),
	url(r'^thanks/$', views.thanks, name = 'thanks'),
	
]