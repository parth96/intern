from django.db import models
# from django.db import IntegrityError

# Create your models here.
class applicationform(models.Model):
    name = models.CharField(max_length=200, null=True)
    bday = models.DateTimeField(blank=True, null=True)
    gender = models.CharField(max_length=1,null=True)
    # category = models.CharField(max_length=4)
    address=models.CharField(max_length=200,null=True)
    phone=models.IntegerField(null=True)
    email=models.EmailField(null=True)
    fname=models.CharField(max_length=20,default='',null=True)
    foccu=models.CharField(max_length=20,default='',null=True)
    # ifemp=models.BooleanField(default=False)
    desig=models.CharField(max_length=20,default='',null=True)
    cpf=models.IntegerField(null=True)
    section=models.CharField(max_length=15,default='',null=True)
    city=models.CharField(max_length=25,default='',null=True)
    phno=models.IntegerField(null=True)
    mono=models.IntegerField(null=True)
    insname=models.CharField(max_length=30,default='',null=True)
    #brname=models.CharField(max_length=30,default='')
    sem=models.IntegerField(null=True)
    semmarks=models.IntegerField(null=True)
    # classpercent=models.DecimalField(max_digits=2, decimal_places=2)
    # approved=models.BooleanField(default=False)
    menname=models.CharField(max_length=20,null=True)
    des1=models.CharField(max_length=20,null=True)
    site=models.CharField(max_length=20,null=True)
    loc=models.CharField(max_length=20,null=True)

