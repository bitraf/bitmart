from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django import forms
from django.forms import ModelForm

from cashregister.models import User, Product, SalesTransaction, Restocking

class RestockForm(forms.Form):
    product_name = forms.CharField(max_length=30)
    amount = forms.CharField()
    net_unit_cost = forms.CharField(max_length=10)

def restock(request):
    if request.method == 'POST':
        form = RestockForm(request.POST)
        if form.is_valid():

            # Create a new Restocking object.
	    product_name = form.cleaned_data['product_name']
	    amount = form.cleaned_data['amount']
	    net_unit_cost = form.cleaned_data['net_unit_cost']

#	    product = Product.objects.filter(name = product_name)

#	    Restocking(timestamp=no



	    return HttpResponseRedirect('/clerk/products/')

    form = RestockForm()

    variables = RequestContext(request, {
        'form': form,
    })

    return render_to_response('clerk/restock.html', variables)
