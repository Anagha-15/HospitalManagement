from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
   path('',views.index,name='Home'),
   path('About',views.About,name='About'),
   path('Booking',views.Booking,name='Bookings'),
   path('Doctors',views.Doctors,name='Doctors'),
   path('Contact',views.Contact,name='Contact'),
   path('Department',views.departments,name='Department')
]

