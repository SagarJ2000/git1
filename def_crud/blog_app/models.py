from django.db import models

# Create your models here.
class Student(models.Model):
    roll = models.IntegerField()
    fname = models.CharField(max_length=55)
    lname = models.CharField(max_length=44)

