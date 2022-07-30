from django import forms  
from django.forms import ModelForm, fields  
from .models import * 


  
  
class UploadImageAchieveForm(forms.ModelForm):  
    class Meta:  
        # To specify the model to be used to create form  
        model = UploadImageAchieve  
        # It includes all the fields of model  
        fields = '__all__' 
        
class UploadImageDanceForm(forms.ModelForm):  
    class Meta:  
        # To specify the model to be used to create form  
        model = UploadImageDance  
        # It includes all the fields of model  
        fields = '__all__' 
        
class UploadImageArtForm(forms.ModelForm):  
    class Meta:  
        # To specify the model to be used to create form  
        model = UploadImageArt 
        # It includes all the fields of model  
        fields = '__all__' 
        
class UploadImageEventForm(forms.ModelForm):  
    class Meta:  
        # To specify the model to be used to create form  
        model = UploadImageEvent  
        # It includes all the fields of model  
        fields = '__all__' 
        
class UploadImageStudioForm(forms.ModelForm):  
    class Meta:  
        # To specify the model to be used to create form  
        model = UploadImageStudio  
        # It includes all the fields of model  
        fields = '__all__'  