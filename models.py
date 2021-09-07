# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from time import timezone

from django.db import models


# Create your models here.


# class Project1(models.Model):
#     name = models.CharField(max_length=255,
#                             unique=True)  # MySQL does not allow unique CharFields to have a max_length > 255
#     creation_date = models.DateTimeField(default=datetime.now)
#
#     def __str__(self):
#         return str(self.name)

class Project1(models.Model):

    name = models.CharField(max_length=255, default='', blank=True)
    age = models.IntegerField(default=None, blank=True, null=True)
    address1 = models.CharField(max_length=255, default='', blank=True)
    address2 = models.CharField(max_length=255,  default='', blank=True)
    city = models.CharField(max_length=255,  default='', blank=True)
    state = models.CharField(max_length=255,  default='', blank=True)
    creation_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.id)
