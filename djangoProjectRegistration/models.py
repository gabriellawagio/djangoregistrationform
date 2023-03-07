from django.db import models

# create a table called products

class Product(models.Model):
    prod_name = models.CharField(max_length=30, blank=False, null=False)
    prod_quantity = models.CharField(max_length=30, blank=False, null=False)
    prod_price = models.CharField(max_length=30, blank=False, null=False)

def __str__(self):
    return self.prod_nameg


# create a table called suppliers
class Supplier(models.Model):
    supp_name = models.CharField(max_length=30, blank=False, null=False)
    supp_email = models.EmailField(max_length=30, blank=False, null=False)
    supp_phonenumber = models.IntegerField(blank=False, null=False)

def __str__(self):
    return self.supp_name