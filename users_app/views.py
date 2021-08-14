from django.shortcuts import render, redirect
from .models import user

def index(request):
    context = {
    	"all_users": user.objects.all()
    }
    return render(request,'index.html', context)# Create your views here.

def submit(request):
    
    user.objects.create(first_name=request.POST["fname"],last_name = request.POST["lname"],email_address=request.POST["email"],age=request.POST["age"])
    return redirect ("/")

