from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django import forms
from django.forms import ModelForm

from cashregister.models import User, Product, SalesTransaction, Restocking

def edit(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ProductDetailForm(request.POST, request.FILES, instance = product)
        if form.is_valid():

            # Create a new Server object.
            form.save()
	    return HttpResponseRedirect('/clerk/products/')
    else:
        form = ProductDetailForm(instance = product)

    variables = RequestContext(request, {
        'form': form,
	'product': product
    })

    return render_to_response('clerk/productdetail.html', variables)

def new(request):
    if request.method == 'POST':
        form = ProductDetailForm(request.POST, request.FILES)
        if form.is_valid():

            # Create a new Server object.
            form.save()
	    return HttpResponseRedirect('/clerk/products/')
    else:
        form = ProductDetailForm()

    variables = RequestContext(request, {
        'form': form,
    })

    return render_to_response('clerk/productdetail.html', variables)

class ProductDetailForm(ModelForm):
    def clean_image(self):
	image = self.cleaned_data.get('image', False)
	if not self.instance.image == image:
	    return None

    class Meta:
	model = Product


