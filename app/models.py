from django.db import models

# Create your models here.

class School(models.Model):
    scname=models.CharField(max_length=100)
    scprincipal=models.CharField(max_length=100)
    sloc=models.CharField(max_length=100)

    def __str__(self):
        return self.scname

