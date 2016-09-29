from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentForm, UserForm, StudentLoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django import forms

def index(request):
    return HttpResponse('Hello There.')

def thanks(request):
    return HttpResponse('Thank You for your form submission.')

def error(request):
    return HttpResponse('You are in the Error Page.')

def loggedIn(request):
    return HttpResponse('You have successfuly logged in.')



def student_signup(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        
        # create a form instance and populate it with data from the request:
        us_form = UserForm(request.POST, request.FILES)
        st_form = StudentForm(request.POST, request.FILES)


        # check whether it's valid:

        if us_form.is_valid():
            if st_form.is_valid():
                username  = us_form.cleaned_data['username']
                password = us_form.cleaned_data['password']
                email  = us_form.cleaned_data['email']
                first_name  = us_form.cleaned_data['first_name']
                last_name = us_form.cleaned_data['last_name']

                user = User.objects.create_user(username, email,password)
                user.first_name = first_name
                user.last_name = last_name
                user.save()           
                st = st_form.save()
                st.user = user
                st.save()

                return HttpResponseRedirect('/sms/thanks/')

            return HttpResponseRedirect('/sms/error/')
    # if a GET (or any other method) we'll create a blank form
    else:
        usr = User.objects.get(pk=1)
        data={'user':usr}
        st_form = StudentForm(initial=data)
        us_form = UserForm()

    return render(request, 'school/st_signup.html', {'us_form':us_form , 'st_form':st_form })



def student_login(request):


    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/sms/loggedIn/')

        else:

            return HttpResponseRedirect('/sms/error/')


    else:

        us_form = StudentLoginForm()

    return render(request, 'school/st_login.html', {'us_form':us_form})    





