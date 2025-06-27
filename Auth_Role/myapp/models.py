from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    class USR_ROLE(models.TextChoices):
        CUSTOMER = 'customer','Customer'
        AGENCY = 'agency','Agency'
        OWNER = 'owner','Owner'
        

    user_role = models.CharField(max_length=8,choices=USR_ROLE.choices)
    

class Property(models.Model):
    
    class PROPERTY_TYPE(models.TextChoices):
        HOME = 'home','Home'
        HOSTEL = 'hostel','Hostel'
        APARTMENT = 'apartment','Apartment'
        OTHER = 'other','other'
    
    property_type = models.CharField(max_length=9,choices=PROPERTY_TYPE.choices)    
    name = models.CharField(max_length=100)
    posted_by = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    

