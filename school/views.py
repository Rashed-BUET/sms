from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentForm, UserForm

def index(request):
	return HttpResponse('Hello There.')


def student_signup(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        # form = NameForm(request.POST)
        # # check whether it's valid:
        # if form.is_valid():
        #     # process the data in form.cleaned_data as required
        #     # ...
        #     # redirect to a new URL:
        return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        st_form = StudentForm()
        us_form = UserForm()

    return render(request, 'school/st_signup.html', {'st_form': st_form, 'us_form':us_form })