from django.contrib import admin

from cashregister.models import User, Product, SalesTransaction, Restocking

admin.site.register(User)
admin.site.register(Product)
