from django.shortcuts import render_to_response, get_object_or_404

from cashregister.models import User, Product, SalesTransaction, Restocking

def store(request):
    available_products = Product.objects.all().filter(stock__gte=1)
    return render_to_response('cashregister/store.html', {'available_products': available_products})
