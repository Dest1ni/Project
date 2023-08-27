from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
# Create your models here.

#class MyCustomUser(AbstractUser):
#   pass
UserModel: AbstractUser = get_user_model()