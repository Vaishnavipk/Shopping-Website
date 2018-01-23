from django.contrib import admin

# Register your models here.
from main.models import Product,BuyUser


admin.site.register(Product)
admin.site.register(BuyUser)