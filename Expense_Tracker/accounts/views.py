from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.


def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('register')

            if User.objects.filter(email=email).exists():
                messages.info(request, "Email Taken")
                return redirect('register')
            else:
                user =User.objects.create_user(first_name=first_name, last_name=last_name, username=username, password=password1, email=email)
                user.save()
                return redirect('login')

        else:
            messages.info(request,"Password not matching ")
  
    return render(request,'accounts/register.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password= password) # if user exists it will give user object 

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,'Invalid username or password')
            return redirect ('login')


    return render(request, 'accounts/login.html')

def logout(request):
    auth.logout(request)
    return redirect("/")