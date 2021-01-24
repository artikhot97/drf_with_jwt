# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class User(AbstractUser):
    username = models.CharField(blank=True, null=True,max_length=30)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return "{}".format(self.email)

"""
UserManger is Custom User models
"""
class UserManager(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='manger')
    company = models.CharField(max_length=5)
    dob = models.DateField()
    address = models.CharField(max_length=255)


"""
UserEmpolyee is Custom User models
"""
class UserEmpolyee(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='empolyee')
    company = models.CharField(max_length=5)
    dob = models.DateField()
    address = models.CharField(max_length=255)
    mobile = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

