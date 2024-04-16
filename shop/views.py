from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,"shop/index.html")

def about(request):
    return HttpResponse("Know about us .....")

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