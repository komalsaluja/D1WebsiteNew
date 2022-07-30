from django.db import models

class UploadImageAchieve(models.Model):
    caption = models.TextField(null=True,default=None,blank=True)
    image = models.ImageField(upload_to='achieveimages')
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.caption
    
class UploadImageDance(models.Model):
    caption = models.TextField(null=True,default=None,blank=True)
    image = models.ImageField(upload_to='danceimages')
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.caption
    
class UploadImageArt(models.Model):
    caption = models.TextField(null=True,default=None,blank=True)
    image = models.ImageField(upload_to='artimages')
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.caption
    
class UploadImageEvent(models.Model):
    caption = models.TextField(null=True,default=None,blank=True)
    image = models.ImageField(upload_to='eventimages')
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.caption
    
class UploadImageStudio(models.Model):
    caption = models.TextField(null=True,default=None,blank=True)
    image = models.ImageField(upload_to='studioimages')
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.caption
