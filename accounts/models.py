from distutils.command.upload import upload
from email.policy import default
from django.db import models

# Create your models here.
from django.db import models
from django.contrib import auth

# Create your models here.
class User(auth.models.User,auth.models.PermissionsMixin):
    def __str__(self):
        return "@{}".format(self.username)
class photo(models.Model):
    image=models.ImageField(upload_to='images/')