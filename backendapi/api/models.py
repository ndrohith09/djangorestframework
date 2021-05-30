from django.db import models
import rest_framework

# Create your models here.
class Book(models.Model):
    title = models.TextField(max_length=100 , blank = False , null = False)

class Employee(models.Model):
    fullname = models.CharField(max_length=20)
    emp_code = models.CharField(max_length=3)
    mobile = models.CharField(max_length= 15)

class Worker(models.Model):
    fullname = models.CharField(max_length=20)
    emp_code = models.CharField(max_length=3)
    mobile = models.CharField(max_length= 15)

