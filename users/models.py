from typing import Any
from django.db import models

# Create your models here.
class BloodBank(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    number = models.BigIntegerField()
    bloodGroup = models.CharField(max_length=5)
