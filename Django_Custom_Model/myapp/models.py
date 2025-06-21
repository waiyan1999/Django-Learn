from django.db import models
from myapp.manager import CustomUserManger
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser): 
    
    username = None
    email = models.EmailField(unique=True)
    
    is_agency = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=True)
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManger()
    
    def __str__(self):
        return self.email
    
    
