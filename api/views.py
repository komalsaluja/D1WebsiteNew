from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout ,login
from frontend.forms import ContactForm
from frontend.models import *
from datetime import datetime
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse

from .forms import *
from .models import *

# Create your views here.

def adminPage(request):
    if request.user.is_anonymous:
        return redirect(reverse('login')) 
            
    return render(request,'api/adminPage.html')   


def add_show(request):
    if request.user.is_anonymous:
        return redirect(reverse('login')) 
    
    form_class = ContactForm
    fm = form_class(request.POST or None)
    if request.method == "POST":       
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            phone = fm.cleaned_data['phone']
            msg = fm.cleaned_data['msg']
            reg = Contact(name=name, email=email,phone=phone, msg=msg, date=datetime.now())
            
            reg.save()
            
            messages.success(request,'Data Added')
            return HttpResponseRedirect(reverse('add_show'))
    else:
        fm=ContactForm()
    
    stud = Contact.objects.all()
        
       
    return render(request,'api/add_show.html',{'form':fm, 'stu':stud})
    
   
    
def index(request):
     return render(request, 'api/index.html')
     

def loginUser(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            
            user = authenticate(username=username, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('add_show'))        
            else:
                return render(request,'api/login.html')
        return render(request , "api/login.html")
    else:
        return HttpResponseRedirect(reverse('add_show'))

def logoutUser(request):
    logout(request)
    return redirect(reverse('login'))

def update_data(request, id):
    if request.user.is_anonymous:
        return redirect(reverse('login')) 
    
    if request.method=='POST':
        pi = Contact.objects.get(pk=id)
        fm = ContactForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect(reverse('add_show'))
    else:
        pi=Contact.objects.get(pk=id)
        fm=ContactForm(instance=pi)
        
    
    return render(request, 'api/updateStu.html' ,{'form':fm})

def delete_data(request, id):
    if request.user.is_anonymous:
        return redirect(reverse('login')) 
    
    if request.method == 'POST':
        pi = Contact.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect(reverse('add_show'))
    

# old password needed
def user_change_pass(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm = PasswordChangeForm(user = request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                messages.success(request,"Password Changed Successfully")
                return HttpResponseRedirect(reverse('add_show'))
        else:
            fm=PasswordChangeForm(user=request.user)
        return render(request ,'api/changepass.html',{'form':fm})
    else:
        return HttpResponseRedirect(reverse('login'))
    

def image_upload(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = UploadImageAchieveForm(request.POST, request.FILES)
            if fm.is_valid():
                fm.save()
                
                # Getting the current instance object to display in the template  
                img_object = fm.instance
                
                messages.success(request,'Image Added Successfully')
                # return HttpResponseRedirect(reverse('imageupload'))
                return render(request,'api/image_form.html',{'form':fm,'img_obj':img_object})
        else:
            fm = UploadImageAchieveForm()
        
        return render(request,'api/image_form.html',{'form':fm})
    else:
        return HttpResponseRedirect(reverse('login'))
    
def image_view(request):
     if request.user.is_authenticated:
         form=UploadImageAchieveForm()
         img = UploadImageAchieve.objects.all()
         return render(request,'api/image_view.html',{'form':form,'img':img})
     else:
         return HttpResponseRedirect(reverse('login'))

def image_dance_view(request):
     if request.user.is_authenticated:
         form=UploadImageDanceForm()
         img = UploadImageDance.objects.all()
         return render(request,'api/image_dance_view.html',{'form':form,'img':img})
     else:
         return HttpResponseRedirect(reverse('login'))
     
def image_art_view(request):
     if request.user.is_authenticated:
         form=UploadImageArtForm()
         img = UploadImageArt.objects.all()
         return render(request,'api/image_art_view.html',{'form':form,'img':img})
     else:
         return HttpResponseRedirect(reverse('login'))
     
def image_event_view(request):
     if request.user.is_authenticated:
         form=UploadImageEventForm()
         img = UploadImageEvent.objects.all()
         return render(request,'api/image_event_view.html',{'form':form,'img':img})
     else:
         return HttpResponseRedirect(reverse('login'))
     
def delete_image(request, id):
    if request.user.is_anonymous:
        return redirect(reverse('login')) 
    
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = UploadImageAchieve.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect(reverse('imageview'))

def delete_dance_image(request, id):
    if request.user.is_anonymous:
        return redirect(reverse('login')) 
    
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = UploadImageDance.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect(reverse('imagedanceview'))
        
def delete_art_image(request, id):
    if request.user.is_anonymous:
        return redirect(reverse('login')) 
    
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = UploadImageArt.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect(reverse('imageartview'))
        
def delete_event_image(request, id):
    if request.user.is_anonymous:
        return redirect(reverse('login')) 
    
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = UploadImageEvent.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect(reverse('imageeventview'))
        
def update_image(request, id):
    if request.user.is_anonymous:
        return redirect(reverse('login')) 
    
    if request.user.is_authenticated:
        if request.method=='POST':
            pi = UploadImageAchieve.objects.get(pk=id)
            fm = UploadImageAchieveForm(request.POST, request.FILES,instance=pi)
            if fm.is_valid():
                fm.save()
            return HttpResponseRedirect(reverse('imageview'))
        else:
            pi=UploadImageAchieve.objects.get(pk=id)
            fm=UploadImageAchieveForm(instance=pi)
            
        
        return render(request, 'api/updateImage.html' ,{'form':fm})
    
def update_dance_image(request, id):
    if request.user.is_anonymous:
        return redirect(reverse('login')) 
    
    if request.user.is_authenticated:
        if request.method=='POST':
            pi = UploadImageDance.objects.get(pk=id)
            fm = UploadImageDanceForm(request.POST, request.FILES,instance=pi)
            if fm.is_valid():
                fm.save()
            return HttpResponseRedirect(reverse('imagedanceview'))
        else:
            pi=UploadImageDance.objects.get(pk=id)
            fm=UploadImageDanceForm(instance=pi)
            
        
        return render(request, 'api/updateImage.html' ,{'form':fm})

def update_art_image(request, id):
    if request.user.is_anonymous:
        return redirect(reverse('login')) 
    
    if request.user.is_authenticated:
        if request.method=='POST':
            pi = UploadImageArt.objects.get(pk=id)
            fm = UploadImageArtForm(request.POST, request.FILES,instance=pi)
            if fm.is_valid():
                fm.save()
            return HttpResponseRedirect(reverse('imageartview'))
        else:
            pi=UploadImageArt.objects.get(pk=id)
            fm=UploadImageArtForm(instance=pi)
            
        
        return render(request, 'api/updateImage.html' ,{'form':fm})
    
def update_event_image(request, id):
    if request.user.is_anonymous:
        return redirect(reverse('login')) 
    
    if request.user.is_authenticated:
        if request.method=='POST':
            pi = UploadImageEvent.objects.get(pk=id)
            fm = UploadImageEventForm(request.POST, request.FILES,instance=pi)
            if fm.is_valid():
                fm.save()
            return HttpResponseRedirect(reverse('imageeventview'))
        else:
            pi=UploadImageEvent.objects.get(pk=id)
            fm=UploadImageEventForm(instance=pi)
            
        
        return render(request, 'api/updateImage.html' ,{'form':fm})
        
  
def image_dance_upload(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = UploadImageDanceForm(request.POST, request.FILES)
            if fm.is_valid():
                fm.save()
                
                # Getting the current instance object to display in the template  
                img_object = fm.instance
                
                messages.success(request,'Image Added Successfully')
                # return HttpResponseRedirect(reverse('imageupload'))
                return render(request,'api/image_form_dance.html',{'form':fm,'img_obj':img_object})
        else:
            fm = UploadImageDanceForm()
        
        return render(request,'api/image_form_dance.html',{'form':fm})
    else:
        return HttpResponseRedirect(reverse('login')) 
    
def image_art_upload(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = UploadImageArtForm(request.POST, request.FILES)
            if fm.is_valid():
                fm.save()
                
                # Getting the current instance object to display in the template  
                img_object = fm.instance
                
                messages.success(request,'Image Added Successfully')
                # return HttpResponseRedirect(reverse('imageupload'))
                return render(request,'api/image_form_art.html',{'form':fm,'img_obj':img_object})
        else:
            fm = UploadImageArtForm()
        
        return render(request,'api/image_form_art.html',{'form':fm})
    else:
        return HttpResponseRedirect(reverse('login'))
    
def image_event_upload(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = UploadImageEventForm(request.POST, request.FILES)
            if fm.is_valid():
                fm.save()
                
                # Getting the current instance object to display in the template  
                img_object = fm.instance
                
                messages.success(request,'Image Added Successfully')
                # return HttpResponseRedirect(reverse('imageupload'))
                return render(request,'api/image_form_event.html',{'form':fm,'img_obj':img_object})
        else:
            fm = UploadImageEventForm()
        
        return render(request,'api/image_form_event.html',{'form':fm})
    else:
        return HttpResponseRedirect(reverse('login'))
    

def image_studio_upload(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = UploadImageStudioForm(request.POST, request.FILES)
            if fm.is_valid():
                fm.save()
                
                # Getting the current instance object to display in the template  
                img_object = fm.instance
                
                messages.success(request,'Image Added Successfully')
                # return HttpResponseRedirect(reverse('imageupload'))
                return render(request,'api/image_form_studio.html',{'form':fm,'img_obj':img_object})
        else:
            fm = UploadImageEventForm()
        
        return render(request,'api/image_form_studio.html',{'form':fm})
    else:
        return HttpResponseRedirect(reverse('login'))
    
def update_studio_image(request, id):
    if request.user.is_anonymous:
        return redirect(reverse('login')) 
    
    if request.user.is_authenticated:
        if request.method=='POST':
            pi = UploadImageStudio.objects.get(pk=id)
            fm = UploadImageStudioForm(request.POST, request.FILES,instance=pi)
            if fm.is_valid():
                fm.save()
            return HttpResponseRedirect(reverse('imagestudioview'))
        else:
            pi=UploadImageStudio.objects.get(pk=id)
            fm=UploadImageStudioForm(instance=pi)
            
        
        return render(request, 'api/updateImage.html' ,{'form':fm})
    

def delete_studio_image(request, id):
    if request.user.is_anonymous:
        return redirect(reverse('login')) 
    
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = UploadImageStudio.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect(reverse('imagestudioview'))
        
def image_studio_view(request):
     if request.user.is_authenticated:
         form=UploadImageStudioForm()
         img = UploadImageStudio.objects.all()
         return render(request,'api/image_studio_view.html',{'form':form,'img':img})
     else:
         return HttpResponseRedirect(reverse('login'))
    
        
    
    