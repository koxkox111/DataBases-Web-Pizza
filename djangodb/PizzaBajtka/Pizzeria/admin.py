from django.contrib import admin
from .models import *

admin.site.register(Product)
admin.site.register(Pizza)
admin.site.register(Order)
admin.site.register(Ingredient)
admin.site.register(PizzaSize)
admin.site.register(PizzaOrder)
