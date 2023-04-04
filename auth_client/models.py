from django.db import models

from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.


class Users(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255)
    createdAt = models.DateField(auto_now_add=True)
    updatedAt = models.DateField(auto_now=True)

    def __str__(self):
        return self.first_name


class UsersCows(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    createdAt = models.DateField(auto_now_add=True)
    updatedAt = models.DateField(auto_now=True)

class UsersCalves(models.Model):
    calf_name = models.CharField(max_length=255)
    calf_breed = models.CharField(max_length=255)
    calf_user = models.ForeignKey(Users, on_delete=models.CASCADE)
    calf_cow = models.ForeignKey(UsersCows, on_delete=models.CASCADE)
    createdAt = models.DateField(auto_now_add=True)
    updatedAt = models.DateField(auto_now=True)
