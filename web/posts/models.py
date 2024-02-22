from django.db import models
from customauth.models import UserModel
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(default="My text")
    user = models.ForeignKey(UserModel,on_delete=models.CASCADE,related_name="who_create")
    who_liked = models.ManyToManyField(UserModel,related_name="who_liked")
    who_disliked = models.ManyToManyField(UserModel,related_name='who_disliked')

class Comment(models.Model):
    body = models.TextField(max_length=300)
    user = models.ForeignKey(UserModel,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(UserModel,related_name="likes")