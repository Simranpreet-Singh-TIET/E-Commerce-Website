from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact
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
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        # if(len(name)!=0):
        contact.save()
    return render(request, 'shop/contact.html')

def search(request):
    return render(request,"shop/search.html")
def tracker(request):
    return render(request,"shop/tracker.html")
def productview(request, myid):
    product=Product.objects.filter(id=myid)
    print(product)
    return render(request, "shop/prodview.html",{'product':product[0]})
def checkout(request):
    return render(request,"shop/checkout.html")
    
