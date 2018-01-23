from django.db import models

# Create your models here.
class ShoppningCar(models.Model):
    user = models.CharField(max_length=128)
    item = models.CharField(max_length=128)
    count = models.IntegerField()

    def __str__(self):
        return self.user