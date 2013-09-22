# -*- coding: utf-8 -*- 

from django.db import models

MVA_CHOICES = (
    (0, '0 % - Fritatt'),
    (8, '8 % - Redusert sats'),
    (15, '15 % - Matvaresats'),
    (25, '25 % - Ordinær sats'),
)

class User(models.Model):
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    AUTH_TYPE_CHOICES = (
        (0, 'None'),
        (1, 'p2k12'),
        (2, 'Password'),
        )
    auth_type = models.IntegerField(choices = AUTH_TYPE_CHOICES)

    is_admin = models.BooleanField(default = False)

    def __unicode__(self):
        return self.username

class ProductCategory(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    picture = models.ImageField(upload_to='product_pictures/')

    category = models.ForeignKey(ProductCategory)

    stock = models.IntegerField(default = 0)

    gross_unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    mva_rate = models.IntegerField(choices = MVA_CHOICES, default = 15)

    # Find price without MVA
    def net_unit_price(self):
        return round( float(self.gross_price) / (1 + float(self.mva_rate) / 100), 2)

    def __unicode__(self):
        return self.name 

    

class SalesTransaction(models.Model):
    timestamp = models.DateTimeField()
    reversal = models.BooleanField(default=False)

    TRANSACTION_STATE = (
        (0, 'PENDING'),
        (1, 'COMPLETED'),
        (2, 'CANCELLED'),
    )
    state = models.IntegerField(choices = TRANSACTION_STATE, default = 0)

#    user = models.ForeignKey(User)

    # Net price is without MVA    
    net_total_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_mva = models.DecimalField(max_digits=10, decimal_places=2)

    gross_total_price = models.DecimalField(max_digits=10, decimal_places=2)

    total_items = models.IntegerField()

    def __unicode__(self):
        return 'Sale %d' % (self.pk)


class SalesTransactionItem(models.Model):
    salestransaction = models.ForeignKey(SalesTransaction, related_name = 'items')
    product = models.ForeignKey(Product)
    amount = models.IntegerField()

    # Remember to multiple these with amount
    net_unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    unit_mva = models.DecimalField(max_digits=10, decimal_places=2)

    def __unicode__(self):
        return 'Sale %d - Item %d' % (self.salestransaction.pk, self.pk)

class Restocking(models.Model):
    timestamp = models.DateTimeField()
    deficit = models.BooleanField(default=False)

    user = models.ForeignKey(User)
    product = models.ForeignKey(Product)
    amount = models.IntegerField()

    # Cost price from supplier, without MVA
    net_unit_cost = models.DecimalField(max_digits=10, decimal_places=2)
