from django.core import validators
from django import forms
from matplotlib import widgets
from .models import Contact

class ContactForm(forms.ModelForm):   
    class Meta:
        model = Contact
        fields = ["name","email","phone","msg"]
        labels = {'name':'Name','email':'Email','phone':'Phone','msg':'Message'}
        
        widgets = {
            'name':forms.TextInput(attrs={'class':'myclass','placeholder':'Enter Your Name'}),
            'email':forms.TextInput(attrs={'class':'myclass','placeholder':'Enter Email-id'}),
            'phone':forms.TextInput(attrs={'class':'myclass','placeholder':'Enter Contact No.'}),
            'msg':forms.Textarea(attrs={'class':'myclass','placeholder':'enter your queries...'})
        }