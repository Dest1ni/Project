from django.db import models
from customauth.models import UserModel
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(default="My text")
    user = models.ForeignKey(UserModel,on_delete=models.CASCADE)