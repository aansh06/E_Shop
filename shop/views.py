from django.shortcuts import render
from django.http import HttpResponse
from . models import Product
from math import ceil




# Create your views here.
def index(request):
    products = Product.objects.all()
    slides = [products[i:i+4] for i in range(0, len(products), 4)]  # Group products into slides

    # Check if the last slide has fewer than 4 products
    if len(products) % 4 != 0:
        remaining_products = len(products) % 4
        last_slide = products[-remaining_products:]
        slides.append(last_slide)
    
    return render(request, 'shop/index.html', {'slides': slides})    

def about(request):
    return render(request,"shop/about.html")

def contact(request):
    return HttpResponse("contact us .....")

def tracker(request):
    return HttpResponse("track your product .....")

def search(request):
    return HttpResponse("Search .....")

def productview(request):
    return HttpResponse("lets shop .....")

def checkout(request):
    return HttpResponse("final .....")