from django.shortcuts import render
from .models import userInformation
from .insertDataForm import InsertDataForm



# Create your views here.
#show users information
def showInformation(request):
    informations= userInformation.objects.all()

    context ={
        'informations' : informations
    }

    return render(request, 'datatemplate/viewinformation.html', context)


#insert users information

def insertInformation(request):

    msg = ""

    insertform = InsertDataForm()
    if request.method =="POST":
        insertform= InsertDataForm(request.POST)
        msg= "Invalid Information. Try again!!"
        if insertform.is_valid():
            insertform.save()
            msg = "Information is included. Now you can insert New Information.."
            insertform = InsertDataForm()

    context = {
        'insertform': insertform
    }

    return render(request, 'datatemplate/insertinformation.html', context)