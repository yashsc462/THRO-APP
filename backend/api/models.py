from django.db import models

# Create your models here.

    


class Vendor(models.Model):
    STATES_CHOICES = [
        ('AN', 'Andaman and Nicobar Islands'),
        ('AP', 'Andhra Pradesh'),
        ('AR', 'Arunachal Pradesh'),
        ('AS', 'Assam'),
        ('BR', 'Bihar'),
        ('CH', 'Chandigarh'),
        ('CT', 'Chhattisgarh'),
        ('DL', 'Delhi'),
        ('GA', 'Goa'),
        ('GJ', 'Gujarat'),
        ('HR', 'Haryana'),
        ('HP', 'Himachal Pradesh'),
        ('JK', 'Jammu and Kashmir'),
        ('JH', 'Jharkhand'),
        ('KA', 'Karnataka'),
        ('KL', 'Kerala'),
        ('LA', 'Ladakh'),
        ('LD', 'Lakshadweep'),
        ('MP', 'Madhya Pradesh'),
        ('MH', 'Maharashtra'),
        ('MN', 'Manipur'),
        ('ML', 'Meghalaya'),
        ('MZ', 'Mizoram'),
        ('NL', 'Nagaland'),
        ('OR', 'Odisha'),
        ('PY', 'Puducherry'),
        ('PB', 'Punjab'),
        ('RJ', 'Rajasthan'),
        ('SK', 'Sikkim'),
        ('TN', 'Tamil Nadu'),
        ('TG', 'Telangana'),
        ('TR', 'Tripura'),
        ('UP', 'Uttar Pradesh'),
        ('UT', 'Uttarakhand'),
        ('WB', 'West Bengal'),
    ]

    vendorName = models.CharField(max_length=100)
    vendorAddress = models.CharField(max_length=200)
    vendorGstNumber = models.CharField(max_length=50)
    vendorPhoneNumber = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2, choices=STATES_CHOICES)
    pincode = models.CharField(max_length=10)

    def __str__(self):
        return self.vendorName




class Customer(models.Model):
    customerFirstName = models.CharField(max_length=100)
    customerMiddleName = models.CharField(max_length=100)
    customerLastName = models.CharField(max_length=100)
    customerAddress = models.CharField(max_length= 200)
    customerPhoneNumber = models.CharField(max_length=20)




class Company(models.Model):
    STATES_CHOICES = [
        ('AN', 'Andaman and Nicobar Islands'),
        ('AP', 'Andhra Pradesh'),
        ('AR', 'Arunachal Pradesh'),
        ('AS', 'Assam'),
        ('BR', 'Bihar'),
        ('CH', 'Chandigarh'),
        ('CT', 'Chhattisgarh'),
        ('DL', 'Delhi'),
        ('GA', 'Goa'),
        ('GJ', 'Gujarat'),
        ('HR', 'Haryana'),
        ('HP', 'Himachal Pradesh'),
        ('JK', 'Jammu and Kashmir'),
        ('JH', 'Jharkhand'),
        ('KA', 'Karnataka'),
        ('KL', 'Kerala'),
        ('LA', 'Ladakh'),
        ('LD', 'Lakshadweep'),
        ('MP', 'Madhya Pradesh'),
        ('MH', 'Maharashtra'),
        ('MN', 'Manipur'),
        ('ML', 'Meghalaya'),
        ('MZ', 'Mizoram'),
        ('NL', 'Nagaland'),
        ('OR', 'Odisha'),
        ('PY', 'Puducherry'),
        ('PB', 'Punjab'),
        ('RJ', 'Rajasthan'),
        ('SK', 'Sikkim'),
        ('TN', 'Tamil Nadu'),
        ('TG', 'Telangana'),
        ('TR', 'Tripura'),
        ('UP', 'Uttar Pradesh'),
        ('UT', 'Uttarakhand'),
        ('WB', 'West Bengal'),
    ]

    companyName = models.CharField(max_length=100)
    companyAddress = models.CharField(max_length=200)
    companyGstNumber = models.CharField(max_length=50)
    companyPhoneNumber = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2, choices=STATES_CHOICES)
    pincode = models.CharField(max_length=10)

    def __str__(self):
        return self.companyName


class Product(models.Model):
    productId = models.CharField(max_length=20,null=True)
    productChoice = [
        ("NULL","NULL"),
        ("THRO","THRO"),
        ("F-PROTEKKT","F-PROTEKKT"),
        ("Vase","Vase")
    ]
    productChoose = models.CharField(max_length=20, choices=productChoice)
    productChoose1 = models.CharField(max_length=20, choices=productChoice,null=True,blank=True)
    productNumber = models.IntegerField()
    productNumber1 = models.IntegerField()
    productImage = models.ImageField(upload_to='static\media',blank=True,null=True)
    productFirstName = models.CharField(max_length=100)
    productDescription = models.CharField(max_length=100)
    productattribute = models.DecimalField(max_digits= 200,decimal_places=2)
    
    productvalue = models.DecimalField(max_digits=50,decimal_places=2)
    


