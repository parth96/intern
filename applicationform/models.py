from django.db import models


# Create your models here.
class applicationform(models.Model):
    name = models.CharField(max_length=200)
    dateofbirth = models.DateField
    gender = models.CharField(max_length=1)
    category = models.CharField(max_length=4)
    address=models.CharField(max_length=200)
    mobileno=models.IntegerField()
    email=models.CharField(max_length=20)
    fname=models.CharField(max_length=20)
    ifemp=models.BooleanField(default=False)
    designation=models.CharField(max_length=20)
    cpf=models.IntegerField()
    section=models.CharField(max_length=15)
    location=models.CharField(max_length=25)
    phoneno=models.IntegerField()
    mobno=models.IntegerField()
    instiname=models.CharField(max_length=30)
    course=models.CharField(max_length=30)
    sem=models.IntegerField()
    sempercentage=models.DecimalField(max_digits=2, decimal_places=2)
    classpercent=models.DecimalField(max_digits=2, decimal_places=2)
    approved=models.BooleanField(default=False)
    mentor=models.CharField(max_length=20)
    designation1=models.CharField(max_length=20)
    site=models.CharField(max_length=20)
    location1=models.CharField(max_length=20)

