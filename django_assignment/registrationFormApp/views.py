from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Registration
from django.contrib import messages
from django.http import Http404

# Create your views here.
def registration_view(request):
    registrationForm = RegistrationForm(request.POST or None)
    context={}
    if request.method == 'POST' and registrationForm.is_valid():
        firstName = registrationForm.cleaned_data['Firstname']
        print(firstName)
        lastName = registrationForm.cleaned_data['Lastname']
        username = registrationForm.cleaned_data['Username']
        password = registrationForm.cleaned_data['Password']
        print(firstName+" "+lastName+" "+username+" "+password)
        # user = Registration.objects.all().delete()
        try:
            user = Registration.objects.filter(username=username)
            print(user.exists())
            if user.exists():
                print("exist")
                # raise Http404("Username already exist ! Try with another username")
                messages.error(request, f'Username already exist ! Try with another username') 
                return render(request,"registration.html",{'registerform':RegistrationForm(),'error':'Username already exist ! Try with another username'})
                #render(request,"registration.html",{'error':'Username already exist ! Try with another username'})
            else:
                print("saved successfully")
                register = Registration(firstname=firstName,lastname=lastName,username=username,password=password)
                register.save()
                return redirect("login")
        except Exception as e:
            print(e)
            # register = Registration(firstname=firstName,lastname=lastName,username=username,password=password)
            # register.save()
            # messages.success(request, f'User create successfully !') 
            # return redirect("login")
    else:
        context={
            'registerform':RegistrationForm()
        }

    return render(request,"registration.html",context)
