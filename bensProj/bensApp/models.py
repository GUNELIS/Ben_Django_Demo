from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class AccountManager(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100) 

# Many to Many field here as managers can have many customers and vice versa. 
class ServiceProvider(models.Model):
    name = models.CharField(max_length=100)
    account_managers = models.ManyToManyField(AccountManager, related_name= 'service_providers')

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    account_managers = models.ManyToManyField(AccountManager, related_name='customers')

# a foreignKey to introduce the relationship between the service and its provider
class Service(models.Model):
    name = models.CharField(max_length=100)
    service_provider = models.ForeignKey(ServiceProvider, related_name='services', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, default= 0.00)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    account_manager = models.ForeignKey(AccountManager, on_delete=models.CASCADE)
    service_provider = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, default=1)
    date = models.DateTimeField(auto_now=True)
    def get_price(self):
        return self.service.price
    
