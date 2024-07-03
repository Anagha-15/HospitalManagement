from django.shortcuts import render
from .models import Departments, doctors
from .forms import BookingForm
# Create your views here.
def index(request):
   
    return render(request,"index.html")

def About(request):
    return render(request,"About.html")
def Booking(request):
    if request.method == "POST":
          form=BookingForm(request.POST)
          if form.is_valid():
               form.save()
               return render(request,'confirmation.html')
    formvalue=BookingForm()
    dict_forms={
        'formkey':formvalue
    }
    return render(request,"Bookings.html",dict_forms)
def Doctors(request):
    dict_docs={
        'doc':doctors.objects.all()
    }
    return render(request,"Doctors.html",dict_docs)
def Contact(request):
    return render(request,"Contact.html")
def departments(request):
    dict_dept={
        'dept':Departments.objects.all()
    }
    return render(request,"Department.html",dict_dept)