from __future__ import absolute_import
from django.db import models

# Create your models here.
class Michael(models.Model):
    name = models.CharField(max_length=50)