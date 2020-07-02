from django.db import models

# Create your models here.
# from .manager import CustomUserManager


class Blog(models.Model):
    user_id = models.IntegerField()
    title = models.CharField(max_length=30)
    body = models.CharField(max_length=1000)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
