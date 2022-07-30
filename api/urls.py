from django.contrib import admin
from django.urls import path 
from api import views
from django.conf import settings  
from django.conf.urls.static import static 



admin.site.site_header = "D1 Dance Fitness and Art Academy Admin"
admin.site.site_title = "D1 Admin Portal" 
admin.site.index_title = "Welcome to D1"

urlpatterns = [
  path('admin/', admin.site.urls),
  path('',views.index,name="index"),
  path('adminPage/',views.adminPage,name="index"),  
  path('add_show/',views.add_show,name="add_show"),  
  path('login/',views.loginUser,name="login"),
  path('logout/',views.logoutUser, name="logout"),
  path('delete/<int:id>/', views.delete_data, name="deletedata"),
  path('update/<int:id>/', views.update_data, name="updatedata"),
  path('changepass/', views.user_change_pass, name="changepass"),
  
  path('images/',views.image_upload, name="imageupload"), # for achieve page
  path('images_view/',views.image_view, name="imageview"),  # for achieve page
  path('deleteimage/<int:id>/', views.delete_image, name="deleteimage"),  # for achieve page
  path('updateimage/<int:id>/', views.update_image, name="updateimage"),  # for achieve page
   
  
  path('imagesdance/',views.image_dance_upload,name="imagedanceupload"),
  path('imagesart/',views.image_art_upload, name="imageartupload"),
  path('imagesevent/',views.image_event_upload, name="imageeventupload"),
   path('imagesstudio/',views.image_studio_upload, name="imagestudioupload"),
  
  path('images_dance_view/',views.image_dance_view, name="imagedanceview"),
  path('images_art_view/',views.image_art_view, name="imageartview"),
  path('images_event_view/',views.image_event_view, name="imageeventview"),
  path('images_studio_view/',views.image_studio_view, name="imagestudioview"),
  
  path('updatedanceimage/<int:id>/', views.update_dance_image, name="updatedanceimage"),
  path('updateartimage/<int:id>/', views.update_art_image, name="updateartimage"),
  path('updateeventimage/<int:id>/', views.update_event_image, name="updateeventimage"),
  path('updatestudioimage/<int:id>/', views.update_studio_image, name="updatestudioimage"),
  
  path('deletedanceimage/<int:id>/', views.delete_dance_image, name="deletedanceimage"),
  path('deleteartimage/<int:id>/', views.delete_art_image, name="deleteartimage"),
  path('deleteeventimage/<int:id>/', views.delete_event_image, name="deleteeventimage"),
  path('deletestudioimage/<int:id>/', views.delete_studio_image, name="deletestudioimage"),  
 
  
]


urlpatterns += static(settings.MEDIA_URL ,document_root = settings.MEDIA_ROOT)   

# when debug=True
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL ,document_root = settings.STATIC_ROOT) 