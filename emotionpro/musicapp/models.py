from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    phone=models.IntegerField()
    address = models.CharField(max_length=200)
    profilepic=models.FileField(upload_to='profile/',blank=True,null=True)


