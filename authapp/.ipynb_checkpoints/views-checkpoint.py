from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def indexPage(request):
    return render(request,"Index.html")

def loginUser(request):
    if request.method=='POST':
        email = request.POST['email']
        password = request.POST['password']
        user=None
        
        if email:
            username = User.objects.get(email=email.lower()).username
            user=authenticate(request,username=username,password=password)
        error=False
        
        

        if user:
            login(request,user)
            return HttpResponseRedirect("/dashboard/")
        else:
            error=True
            return render(request,'Index.html',{'error':error})

    return render(request,'Index.html')
    
def logoutUser(request):
    if(request.user):
        logout(request)
        return HttpResponseRedirect("/")
    return render(request,'Index.html')

@login_required
def Dashboard(request):
    return render(request,"Dashboard.html")
    