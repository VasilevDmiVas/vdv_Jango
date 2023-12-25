from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    email = models.EmailField()
    countUsers = models.IntegerField()

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=150)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)