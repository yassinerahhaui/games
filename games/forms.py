from django import forms
from .models import Contact


class ContactMe(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ['email','message']