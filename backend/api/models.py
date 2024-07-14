from django.db import models

# Create your models here.

    


class Vendor(models.Model):
    vendorName = models.CharField(max_length=100)
    vendorAddress = models.CharField(max_length= 200)
    vendorGstNumber = models.CharField(max_length=50)
    vendorPhoneNumber = models.CharField(max_length=20)



class Customer(models.Model):
    customerFirstName = models.CharField(max_length=100)
    customerMiddleName = models.CharField(max_length=100)
    customerLastName = models.CharField(max_length=100)
    customerAddress = models.CharField(max_length= 200)
    customerPhoneNumber = models.CharField(max_length=20)
