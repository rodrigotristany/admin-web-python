from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class Owner(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return f"Hola {self.first_name}!"
