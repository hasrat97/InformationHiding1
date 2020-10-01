from django.shortcuts import render, redirect
from .models import RealUser
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def viewUserList(request):

    allUsers = RealUser.objects.all()

    context={
        'allUsers' : allUsers,
    }

    return render(request, 'RealUserView/realuserview.html', context)



def registrationFunction(request):

    registrationform = UserCreationForm()

    if request.method =="POST":
        registrationform= UserCreationForm(request.POST)
        if registrationform.is_valid():
            registrationform.save()
            return redirect('login')

    context= {

        'registrationform' :  registrationform

    }

    return render (request, 'RegistrationForm/registrationform.html', context)