from django.contrib import admin
from .models import Manufacturer
from .models import Product
from .models import Order
from .models import OrderItem


admin.site.register(Product)
admin.site.register(Manufacturer)
admin.site.register(Order)
admin.site.register(OrderItem)