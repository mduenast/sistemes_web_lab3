from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Sobre(models.Model):
    amount = models.IntegerField()
    date = models.DateField()
    concept = models.TextField(max_length=50)
