from django.db import models

# Create your models here.

class Clients(models.Model):

    name = models.CharField(max_length=64, null=True)
    email = models.EmailField(max_length=64, null=True)
    message = models.CharField(max_length=100,null=True)
