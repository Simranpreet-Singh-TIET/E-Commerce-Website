from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil
def index(request):
    # return HttpResponse("Shop Index")
    # product=Product.objects.all()
    # print(product)
    # n=len(product)
    # nSlides=n//4+ceil((n/4)-(n//4))
    # allprods=[[product,range(1,nSlides),nSlides],[product,range(1,nSlides),nSlides]]
    allprods=[]
    catprods=Product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        product=Product.objects.filter(category=cat)
        n=len(product)
        nSlides= n//4 + ceil((n/4)-(n//4))
        allprods.append([product,range(1,nSlides),nSlides])
    params={'allProds':allprods}
    # params={'no_of_slides':nSlides,'range':range(1,nSlides),'product':products}
    return render(request,'shop/index.html',params)

# Create your views here.
def about(request):
    return render(request,"shop/about.html")

def contact(request):
    return HttpResponse("Shop Contact")

def search(request):
    return HttpResponse("Shop Search")
def tracker(request):
    return HttpResponse("Shop Tracker")
def productview(request):
    return HttpResponse("Shop Product View")
def checkout(request):
    return HttpResponse("Shop Checkout")
    
