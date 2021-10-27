from django.contrib import admin

#from LaCasa.LaCasaDelLiqour.apps import LacasadelliqourConfig
from .models import Products,ShippingAddress,OrderItem,Order,Customer

# Register your models here.
admin.site.register(Products)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
