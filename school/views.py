from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentForm, UserForm

def index(request):
    return HttpResponse('Hello There.')

def thanks(request):
    return HttpResponse('Thank You for your form submission.')



def student_signup(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        us_form = StudentForm(request.POST)
        st_form = UserForm(request.POST)
        # check whether it's valid:
        if us_form.is_valid():
            us_form.save();
            if st_form.is_valid():
                st_form.save()

                
        	return HttpResponseRedirect('/sms/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        st_form = StudentForm()
        us_form = UserForm()

    return render(request, 'school/st_signup.html', {'st_form': st_form, 'us_form':us_form })