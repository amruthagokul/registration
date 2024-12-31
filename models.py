from django.db import models

# Create your models here.

class  student(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    phone=models.IntegerField()
    age=models.CharField(max_length=20)
    course=models.CharField(max_length=20,default="python")
    