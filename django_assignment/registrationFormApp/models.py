from django.db import models

# Create your models here.
class Registration(models.Model):
    id=models.AutoField(primary_key=True,null=False,)
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)