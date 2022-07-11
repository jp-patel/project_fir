from django import forms
from .models import jurisdictionModel, reportModel

class jurisdictionForm(forms.ModelForm):
    class Meta:
        model = jurisdictionModel
        fields = ['division']

class reportForm(forms.ModelForm):
    class Meta:
        model = reportModel
        # exclude = ['officer', 'date', 'status']
        fields = ['division', 'subject', 'concern', 'address', 'intersection', 'day', 'time', 'frequency', 'complainee', 'complainee_address', 'city', 'pincode', 'phone', 'civilian']
