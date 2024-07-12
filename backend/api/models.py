from django.db import models

# Create your models here.
class user(models.Model):    # Created model for paasing login page  data for auth in the models 
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)