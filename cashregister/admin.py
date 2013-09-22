from django.contrib import admin

from cashregister.models import User, Product, SalesTransaction, SalesTransactionItem, Restocking, ProductCategory

admin.site.register(User)
admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Restocking)
admin.site.register(SalesTransaction)
admin.site.register(SalesTransactionItem)
