from django.shortcuts import render
from .models import *
# Create your views here.


def product(request):
    products=Product.objects.all()
    return render(request,'products.html',{'product':products})
#,{'product':product}