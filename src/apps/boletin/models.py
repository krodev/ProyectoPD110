from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Registrado(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    email =models.EmailField()
    timestamp =models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):#Python 2
        return self.email

# class Contact(models.Model):
# 	nombre = models.CharField(max_length=60, blank=True, null=True)
# 	email =models.EmailField()
# 	mensaje = models.CharField(max_length=250)