from django.contrib import admin
from django.urls import path, include
from frontend import views
from django.conf import settings  
from django.conf.urls.static import static 

urlpatterns = [
    path('',views.home, name='home' ),
    path('about/',views.about, name='about' ),
     path('studio/',views.studio, name='studio' ),
     path('director/',views.director, name='director' ),
    path('services/',views.services, name='services' ),
    path('achieve/',views.achievements, name='achievements' ),
    path('art/',views.art, name='art' ),
    path('events/',views.events, name='events' ),
    path('contact/',views.contact, name='contact' ),
    path('enquiry/',views.enquiry, name='enquiry' ),
    
    
]
urlpatterns += static(settings.MEDIA_URL ,document_root = settings.MEDIA_ROOT)   

# when debug=True
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL ,document_root = settings.STATIC_ROOT) 