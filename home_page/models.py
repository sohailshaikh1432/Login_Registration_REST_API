from django.db import models

# Create your models here.


class Employee(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.CharField(max_length=250)
    salary = models.IntegerField()
    status = models.BooleanField()
