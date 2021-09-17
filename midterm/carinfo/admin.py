from django.contrib import admin
from carinfo.models import Products

# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'car_model',)
    
admin.site.register(Products, ProductsAdmin)