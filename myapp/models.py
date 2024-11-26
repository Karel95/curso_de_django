from django.db import models

# Create your models here.
class Project(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField()
  
class Task(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField()
  project = models.ForeignKey(Project, on_delete=models.CASCADE)
  