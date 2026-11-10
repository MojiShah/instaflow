from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    class Role(models.TextChoices):
        USER = "user" , "User"
        PREMIUM = "premium", "Premium"
        
    email = models.EmailField(unique=True,null=True,blank=True)
    phone = models.CharField(max_length=15,unique=True,null=True,blank=True)
    bio = models.CharField(max_length=160,blank=True)
    avatar = models.ImageField(upload_to='avatars/',null=True,blank=True)
    role = models.CharField(max_length=20,choices=Role.choices,default=Role.USER)
    
    def __str__(self):
        return self.username
