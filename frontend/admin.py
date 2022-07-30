from django.contrib import admin
from .models import *

class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','phone','msg','date']
    
admin.site.register(Contact,ContactAdmin)