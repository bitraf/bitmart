from tastypie.resources import ModelResource, fields
from tastypie.authorization import Authorization
from cashregister.models import Product, ProductCategory, SalesTransaction, SalesTransactionItem


class CategoryResource(ModelResource):
    class Meta:
        queryset = ProductCategory.objects.all()
        resource_name = 'category'

class ProductResource(ModelResource):
    category = fields.ToOneField( CategoryResource, 'category', full = True )

    class Meta:
        queryset = Product.objects.all()
        resource_name = 'product'


class SaleItemResource(ModelResource):
    product = fields.ToOneField( ProductResource, 'product', full = False )
    class Meta:
        queryset = SalesTransactionItem.objects.all()
        resource_name = 'saleitem'

class SaleResource(ModelResource):
    items = fields.ToManyField(SaleItemResource, 'items', full = True, null = True)
     
    class Meta:
        queryset = SalesTransaction.objects.all()
        resource_name = 'sale'
        authorization = Authorization()
