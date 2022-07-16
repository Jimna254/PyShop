from cgitb import html
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product



def index(request):
    #return HttpResponse("Hello, world. You're at the products index.")
    products = Product.objects.all()
    return render(request, 'index.html',{"products": products})


def new(request):
    #return HttpResponse("New Products")
    products = Product.objects.all()
    return render(request, 'index.html')

