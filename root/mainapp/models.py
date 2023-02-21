from djongo import models
import datetime

class tasks_list(models.Model):
    task = models.CharField(max_length=100)
    status = models.BooleanField()
    date_on_created = models.DateField() 

    

class User(models.Model):
     email = models.EmailField()
     username = models.CharField(max_length=100)
     
     
