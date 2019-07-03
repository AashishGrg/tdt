from django.db import models

from authentication.models import User


#product type
class Product_Type(models.Model):

    product_type_name = models.CharField(max_length=25,unique=True,null=False,blank=False)
    status = models.BooleanField(default=False)
    detail = models.CharField(max_length=250, blank=False)
    product_type_image = models.ImageField(
        null=True, blank=True, upload_to='images/product_type/')

    def __str__(self):
        return self.product_type_name

class Product(models.Model):
    product_name = models.CharField(max_length=50, blank=False)
    product_type = models.ForeignKey(
        Product_Type, on_delete=models.CASCADE, related_name='product_type')
    status = models.BooleanField(default=False)
    detail = models.CharField(max_length=250, blank=False)
    product_image = models.ImageField(
        null=True, blank=True, upload_to='images/product/')
    price = models.FloatField()
    quantity = models.IntegerField()
    users = models.ForeignKey(
        'authentication.User', on_delete=models.CASCADE, related_name='product_user')

    def __str__(self):
        return self.product_name

class ProductTransaction(models.Model):
    TRANSACTION_TYPE = (
        ('Personal_Consumption', 'Personal_Consumption'),
        ('Parent_Child', 'Parent_Child'),
        ('Bad_Debts','Bad_Debts')
    )
    seller = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='seller', blank= False)
    buyer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='buyer', blank= False)
    transaction_type = models.CharField(
        max_length=100, choices=TRANSACTION_TYPE, default="Parent_Child")

    def __str__(self):
        return self.transaction_type
    

