from django.db import models

# Create your models here.
class Teacher(models.Model):
    studentname = models.CharField(max_length=50)
    studentage = models.IntegerField()
    studentlocation = models.CharField(max_length=15)
    
