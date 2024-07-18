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
    product_id = models.CharField(max_length=100)
    product_type = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    count = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    vase_type = models.CharField(max_length=10, blank=True, null=True)
    vase_count = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.product_id  # Display product_id in admin and Django admin

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
    


