from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Empresa(models.Model):
    nom = models.TextField(max_length=50)
    web = models.TextField(max_length=100)

# Create your models here.
class Sobre(models.Model):
    amount = models.IntegerField()
    date = models.DateField()
    concept = models.TextField(max_length=50)
    empresa = models.ForeignKey(Empresa)
    politic = models.ForeignKey(User)

    """def __unicode__(self):
        return self.empresa.non, " " , str(self.empresa.amount), " " , self.sobre.politic.get_user_name()"""