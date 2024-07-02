from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Contact_Us

# Create your views here.
def Home(request):
    return render(request,'index.html')
def Signin(request):
    return render(request,'signin.html')
def About(request):
    return render(request,'about_us.html')
def Contact(request):
    selector={}
    if request.method=='POST':
        selector={
            'selected':request.POST.get['contacting_for']
        }
        if selector['selected']=='Feedback':
            details=Contact_Us.objects.create(
            info_type=request.POST['contacting_for'],
            Fullname_ursername=request.POST['Name_username'],
            Email=request.POST['Email'],
            Issue_quriy=request.POST['issue_feedback'],
            )
        elif selector['selected']=='Quiry':
            details=Contact_Us.objects.create(
            info_type=request.POST['contacting_for'],
            Fullname_ursername=request.POST['Name_username'],
            Email=request.POST['Email'],
            Issue_quriy=request.POST['issue_feedback'],
            )
        elif selector['selected']=='Issues':
            details=Contact_Us.objects.create(
            info_type=request.POST['contacting_for'],
            Fullname_ursername=request.POST['Name_username'],
            Email=request.POST['Email'],
            Issue_quriy=request.POST['issue_feedback'],
            )
        submit=True
        return redirect("/Home")
    return render(request,'contact_us.html',details,{'submit':submit})
def Browse(request):
    return render(request,'search.html')