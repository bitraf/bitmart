from tastypie.resources import ModelResource, fields
from cashregister.models import Product, ProductCategory


class CategoryResource(ModelResource):
    class Meta:
        queryset = ProductCategory.objects.all()
        resource_name = 'category'

class ProductResource(ModelResource):
    category = fields.ToOneField( CategoryResource, 'category', full = True )

    class Meta:
        queryset = Product.objects.all()
        resource_name = 'product'
