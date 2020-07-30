from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login 
from registrationFormApp import models
from django.contrib import messages
# Create your views here.
def login_view(request):
		loginForm = LoginForm(request.POST or None)
		context={}
		if loginForm.is_valid() and request.method =='POST':
			username = loginForm.cleaned_data["username"]
			password = loginForm.cleaned_data["password"]
			print(username+" "+password)
			user = models.Registration.objects.filter(username=username, password=password)
			if user.exists():
    				request.session['username'] = username
    				return redirect("timetable")
			else:
    				return render(request,"login.html",{'form':LoginForm(),'error':'Invalid credentials'})
    				# messages.error(request, f'Invalid ')
				 

			print(user)
    		# return redirect("timetable")
		else:
			context={
				'form':LoginForm()
			}
		# context['form'] = LoginForm()
		return render(request,"login.html",context)