from django.db import models


# Create your models here.


class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField()


class Department(models.Model):
    title = models.CharField(max_length=16)


class Roles(models.Model):
    caption = models.CharField(max_length=16)
