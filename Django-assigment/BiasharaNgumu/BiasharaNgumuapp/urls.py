from django.contrib import admin
from django.urls import path

from BiasharaNgumuapp import views

urlpatterns = [
    # path('admin/', admin.site.urls),
     path('', views.home, name='home'),##this is working
     path('women/', views.women, name='women'),#this is also working 
     path('men/', views.men, name='men'),#this is also working
     path('aboutus/', views.about, name='about'),#this is also working
     path('contacts/', views.contact, name='contact'), #this is also working
]

