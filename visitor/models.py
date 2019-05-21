from django.db import models

# Create your models here.

class Message(models.Model):
    name = models.TextField()
    email = models.TextField()
    title = models.TextField()
    date =  models.DateField()
    content = models.TextField()
    pwd = models.TextField()
