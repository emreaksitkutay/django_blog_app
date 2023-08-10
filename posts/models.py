from django import forms
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

# Create your models here.

class PostManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    is_deleted = models.BooleanField(default=False)
    # objects = PostManager()
    class Meta:
        app_label = 'posts'
    
    def __str__(self):
        return self.title
    
class User(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=150)