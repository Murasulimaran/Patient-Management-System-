from django.db import models

# Create your models here.

class Records(models.Model):
    name = models.CharField(max_length=250)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=250)
    problem = models.CharField(max_length=250)
    status = models.CharField(max_length=250)
    report = models.CharField(max_length=250)
    next_meet = models.DateField()



