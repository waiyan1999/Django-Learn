from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages








def index(request):
    message = messages.success(request,'Welcome!')
    
    return render(request,'index.html')


def logout_user(request):
    logout(request)
    return redirect('index')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        authentication = authenticate(username=username,password=password)
        if authenticate:
            login(request,authentication)
            messages.success(request,'Login Successfully')
            print(messages)
            print('Login Successfully')
            return redirect('index')
        else:
            print("Login Fail")
            messages.error(request,'Wrong User Name and Password')
            print('Login Fail')
            return redirect('index')
            
        
    
    else:
        return redirect('index')