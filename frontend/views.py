from datetime import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render 
from django.contrib import messages
from django.conf import settings

from api.models import *
from .forms import ContactForm
from .models import Contact
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

def home(request):
    context = {
       
    }
    return render(request,'frontend/index.html',context)

def about(request):
    return render(request,'frontend/about.html')

def studio(request):
    img = UploadImageStudio.objects.all()
    return render(request,'frontend/studio.html',{'img':img})

def director(request):
    return render(request,'frontend/director.html')


def services(request):
    img = UploadImageDance.objects.all()
    return render(request,'frontend/services.html',{'img':img})

def events(request):
    img = UploadImageEvent.objects.all()
    return render(request,'frontend/events.html',{'img':img})

def art(request):
    img = UploadImageArt.objects.all()
    return render(request,'frontend/art.html',{'img':img})

def achievements(request):
    img = UploadImageAchieve.objects.all()
    return render(request,'frontend/achieve.html',{'img':img})

def contact(request):
    form_class = ContactForm
    fm = form_class(request.POST or None)
    if request.method == "POST":       
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            phone = fm.cleaned_data['phone']
            msg = fm.cleaned_data['msg']
            email1 = email.lower()
            reg = Contact(name=name, email=email1,phone=phone, msg=msg, date=datetime.now())
            
            reg.save()
            
            template = render_to_string('frontend/email_template.html',{'name':name})
            mail_send = EmailMessage(
                 'Thanks for contacting D1 Academy',
                template,
                settings.EMAIL_HOST_USER, 
                [email1],
                )
            mail_send.fail_silently = False
            mail_send.send()
            
            template1 = render_to_string('frontend/email_template1.html',{'name':name,'email':email1,'phone':phone,'msg':msg})
            mail_send1 = EmailMessage(
                 ' Enquiry Alert !!!,',
                template1,
                settings.EMAIL_HOST_USER, 
                [settings.EMAIL_HOST_USER] ,
                )
            mail_send1.fail_silently = False
            mail_send1.send()
            
        else:
            fm=ContactForm()
            
           
            
        messages.success(request,'Thanks for Contacting Us! Your Message has been sent')
        return HttpResponseRedirect('/contact')
            
    
    return render(request,'frontend/contact.html',{'form':fm})

def enquiry(request):
    form_class = ContactForm
    fm = form_class(request.POST or None)
    if request.method == "POST":       
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            phone = fm.cleaned_data['phone']
            msg = fm.cleaned_data['msg']
            email1 = email.lower()
            reg = Contact(name=name, email=email1,phone=phone, msg=msg, date=datetime.now())
            
            reg.save()
            
            template = render_to_string('frontend/email_template.html',{'name':name})
            mail_send = EmailMessage(
                 'Thanks for contacting D1 Academy',
                template,
                settings.EMAIL_HOST_USER, 
                [email1],
                )
            mail_send.fail_silently = False
            mail_send.send()
            
            template1 = render_to_string('frontend/email_template1.html',{'name':name,'email':email1,'phone':phone,'msg':msg})
            mail_send1 = EmailMessage(
                 ' Enquiry Alert !!!,',
                template1,
                settings.EMAIL_HOST_USER, 
                [settings.EMAIL_HOST_USER] ,
                )
            mail_send1.fail_silently = False
            mail_send1.send()
            
            messages.success(request,'Thanks for Contacting Us! Check your Mail')
            
        else:
            fm=ContactForm()
            
        return HttpResponseRedirect('/')
            
    
    return render(request,'frontend/enquiry.html',{'form':fm})
