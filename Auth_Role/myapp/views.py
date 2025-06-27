from django.shortcuts import render,redirect
from myapp.form import RegisterForm,LoginForm
from django.contrib.auth import login,logout,authenticate

def base(request):
    return render(request,'base.html')

def index(request):
    return render(request,'index.html')

def login_user(request):
    login_form = LoginForm()
    context = {'login_form':login_form}
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        auth = authenticate(username=username,password=password)
        if auth:
            login(request,auth)
            print("Successful login")
        else:
            print("Error occur in Login")
        
        return redirect('index')
    
    else:
        return render(request,'login.html',context)

def register_user(request):
    register_form = RegisterForm()
    context = {'register_form':register_form}
    
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            new_user = register_form.save()
            print('Successfully New User Register')
            login(request,new_user)
            print('Successful Login')
        else:
            print(register_form.errors)
            print('Error Occur in Registartion')
        
        return redirect('index')
            
    else:
        return render(request,'register.html',context)

def logout_user (request):
    logout(request)
    return redirect('index')
