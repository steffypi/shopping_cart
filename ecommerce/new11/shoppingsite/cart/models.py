from django.db import models
from shop.models import Product
from django.contrib.auth.models import User
# Create your models here.
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    products=models.ForeignKey(Product,on_delete=models.CASCADE)
    date_added=models.DateField(auto_now_add=True)
    quantity=models.IntegerField(default=1)
    active=models.BooleanField(default=True)

    def subtotal(self):
        return self.quantity*self.products.price

    def __str__(self):
        return self.products.name


class Account(models.Model):
    accountnumber = models.CharField(max_length=200)
    acctype = models.CharField(max_length=200)
    amount = models.IntegerField()
    def __str__(self):
        return self.accountnumber
        

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    adress = models.TextField()
    phone = models.CharField(max_length=100)
    order_status = models.CharField(max_length=30,default="pending")
    delivery_status = models.CharField(max_length=30,default="pending")
    noofitems = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    def subtotal(self):
        return self.noofitems*self.product.price
        