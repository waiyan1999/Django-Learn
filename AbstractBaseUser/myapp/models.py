from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from myapp.manager import CustomUsreManager


class CustomUser(AbstractBaseUser,PermissionsMixin):
    
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joned = models.DateTimeField(default=timezone.now)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = CustomUsreManager()
    
    def __str__(self):
        return self.email
    
    

    
    
    
    