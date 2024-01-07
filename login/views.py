from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login


# Create your views here.

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            auth_login(request,user)
            return redirect('afs')
        else:
            return redirect('login')
          
    return render(request,"login.html")
        

def afs(request):
    return render(request,"afs.html")

def profile(request):
    en=User.objects.last()
    return render(request,"profile.html",{'en':en})

def sign(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('confirm_password')
        if password!=cpassword:
            return redirect('sign')
        else:
            my_user=User.objects.create_user(username,email,password)
            my_user.save()
        return redirect('login')
        
    return render(request,"sign.html")


def home_page(request):
    return render(request,"home.html")

def groups(request):
    return render(request,"groups.html")


def create_follow(request):  
    return render(request,"create_follow.html")


def error_404(request,exception):
    return render(request,"404.html")
