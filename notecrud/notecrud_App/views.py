from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
def Home(request):
    
    return render(request,'index.html')
def Signin(request):
    return render(request,'signin.html')
def About(request):
    return render(request,'about_us.html')
def Contact(request):
    return render(request,'contact_us.html')