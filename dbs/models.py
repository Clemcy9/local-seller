from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Account(AbstractUser):
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False, unique=True)
    email = models.EmailField(blank=False, unique=True)
    is_staff = models.BooleanField(default=True,)
    # USERNAME_FIELD
    phone_number = models.CharField(max_length=20, blank=False)



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number','last_name']

    
