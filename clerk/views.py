from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.forms import ModelForm
from django.template import RequestContext

from cashregister.models import User, Product, SalesTransaction, Restocking

def products(request):
    all_products = Product.objects.all()
    return render_to_response('clerk/products.html', {'available_products': all_products})


def clerk(request):
    return render_to_response('clerk/clerk.html')
