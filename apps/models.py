from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    owner = models.ForeignKey('auth.User', related_name='profile', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    username = models.CharField(max_length=100,blank=True)
    password = models.CharField(max_length=100,blank=True)
    email = models.EmailField(blank=True)
    start_year = models.IntegerField(blank=True)
    name = models.CharField(max_length=100, blank=True)
    datafile = models.FileField(upload_to='documents/', blank=True)
