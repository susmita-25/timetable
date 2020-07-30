from django.db import models

# Create your models here.
class TimeTable(models.Model):
    id = models.AutoField(primary_key=True)
    day = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
