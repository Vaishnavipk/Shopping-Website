from django.db import models

# Create your models here.
class Product(models.Model):
    item = models.CharField(max_length=128)
    money = models.IntegerField()
    

    def __str__(self):
        return self.item
    
class BuyUser(models.Model):
    user=models.CharField(max_length=128)
    item = models.CharField(max_length=128)
    count = models.IntegerField()
    

    def __str__(self):
        return self.user
    
    