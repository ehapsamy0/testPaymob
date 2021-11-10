from django.db import models

# Create your models here.




class User(models.Model):
    username = models.CharField(max_length=150)


class Project(models.Model):
    name_project = models.CharField(max_length=150)


class Gug(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    rate = models.CharField(max_length=120)
