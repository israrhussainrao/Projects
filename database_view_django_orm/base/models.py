from django.db import models

class Customers(models.Model):
    customer_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100, blank=True, null=True)

class Orders(models.Model):
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    order_date = models.DateField(auto_now_add=True)
