from django import forms
from django.contrib.auth.forms import UserCreationForm
from myapp.models import CustomUser

class RegisterForm(UserCreationForm):
    
    
    class Meta:
        model = CustomUser
        fields = [
            'user_role','username'
        
        ]
        
        
class LoginForm():
    
    username = forms.CharField(max_length=20)
    password = forms.PasswordInput()
    
