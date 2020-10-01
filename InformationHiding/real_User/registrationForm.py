from django import forms
from .models import RealUser

class createRegistrationForm(forms.ModelForm):
    class Meta:
        model = RealUser
        fields = ('userName', 'FirstName', 'LastName', 'Phone_No', 'EmailID')