from django.db import models
from customauth.models import UserModel
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(default="My text")
    user = models.ForeignKey(UserModel,on_delete=models.CASCADE,related_name="who_create")
    who_liked = models.ManyToManyField(UserModel,related_name="who_liked")
    who_disliked = models.ManyToManyField(UserModel,related_name='who_disliked')