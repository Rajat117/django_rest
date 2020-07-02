from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# from .manager import CustomUserManager


class Person(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=50, unique=True)
    gender = models.CharField(max_length=10, choices=[
                              ('M', 'Male'), ('F', 'Female'), ('O', 'Other')
                              ], null=True)
    age = models.IntegerField(null=True)
    username = models.CharField(max_length=15, unique=True, null=True)
    bio = models.TextField(null=True)
    password = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    write_only_fields = ['password']
