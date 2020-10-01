from django import forms
from .models import userInformation

class InsertDataForm(forms.ModelForm):
    class Meta:
        model = userInformation
        fields = ('imageName', 'Image', 'Date', 'Time','realuser')