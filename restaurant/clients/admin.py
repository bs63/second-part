from django.contrib import admin

from .models import Client, Table, Order, Waiter, Dishes, Menu, Review, City

admin.site.register(Client)
admin.site.register(Table)
admin.site.register(Order)
admin.site.register(Waiter)
admin.site.register(Dishes)
admin.site.register(Menu)
admin.site.register(Review)
admin.site.register(City)
