from django import forms
from .models import civilianModel, officerModel

class civilianForm(forms.ModelForm):
    class Meta:
        model = civilianModel
        fields = ['email', 'password']

class civilianProfileForm(forms.ModelForm):
    class Meta:
        model = civilianModel
        exclude = ['email', 'password']
        # fields = ['first_name', 'last_name', 'aadhar', 'address', 'city', 'pincode', 'phone']

class officerForm(forms.ModelForm):
    class Meta:
        model = officerModel
        fields = ['email', 'password']
