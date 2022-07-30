from django.contrib import admin

from .models import *
from django.contrib.sessions.models import Session



class UploadImageAchieveAdmin(admin.ModelAdmin):
    list_display = ['id','caption','image','date']

class UploadImageDanceAdmin(admin.ModelAdmin):
    list_display = ['id','caption','image','date']

class UploadImageArtAdmin(admin.ModelAdmin):
    list_display = ['id','caption','image','date']

class UploadImageEventAdmin(admin.ModelAdmin):
    list_display = ['id','caption','image','date']
    
admin.site.register(UploadImageAchieve,UploadImageAchieveAdmin)
admin.site.register(UploadImageDance,UploadImageDanceAdmin)
admin.site.register(UploadImageArt,UploadImageArtAdmin)
admin.site.register(UploadImageEvent,UploadImageEventAdmin)

admin.site.register(Session)  
