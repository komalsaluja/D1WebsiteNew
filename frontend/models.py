from statistics import mode
from django.db import models
from django.core.validators import RegexValidator

class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=False,null=False) # Validators should be a list
    msg=models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
