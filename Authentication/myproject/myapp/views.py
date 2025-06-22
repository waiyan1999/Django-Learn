from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from myapp.form import RegisterForm








def index(request):
    # message = messages.success(request,'Welcome!')
    return render(request,'index.html')


def logout_user(request):
    logout(request)
    return redirect('index')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        authentication = authenticate(username=username,password=password)
        if authentication:
            login(request,authentication)
            messages.success(request,'Login Successfully')
            print(messages)
            print('Login Successfully')
            return redirect('index')
        else:
            print("Login Fail")
            # messages.error(request,'Wrong User Name and Password')
            print('Login Fail')
            return render(request,'login-form.html')
    else:
        return redirect('index')
    
def register_user(request):
    form = RegisterForm()
    context = {'form':form}
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request,new_user)
            return redirect('index')
            
        else:
            print ('Register Fail')
            return render(request,'register-form.html',context)
    
    return render(request,'register-form.html',context)
    
    