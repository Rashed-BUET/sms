from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^studentsignup/$', views.student_signup, name = 'st_signup'),
	url(r'^studentlogin/$', views.student_login, name = 'st_login'),
	url(r'^loggedIn/$', views.loggedIn, name = 'loggedIn'),
	url(r'^thanks/$', views.thanks, name = 'thanks'),
	url(r'^error/$', views.error, name = 'error'),
	
]