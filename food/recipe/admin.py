from django.contrib import admin

# Register your models here.
from .models import Dish, OrderItem, Order

admin.site.register(Dish)
admin.site.register(OrderItem)
admin.site.register(Order)
