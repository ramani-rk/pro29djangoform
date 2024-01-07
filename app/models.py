from django.db import models

# Create your models here.

class School(models.Model):
    Sname=models.CharField(max_length=100)
    Sprincipal=models.CharField(max_length=100)
    Slocation=models.CharField(max_length=100)

    def __str__(self):
        return self.Sname

class WebForm (models.Model):
    date=models.DateField()
    author=models.CharField(max_length=100)