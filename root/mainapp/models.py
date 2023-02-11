from django.db import models

# Create your models here.

class entry(models.Model):
    num = models.IntegerField(default=0)
    name = models.CharField(max_length=50)

