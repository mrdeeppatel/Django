from django.shortcuts import render
from .models import Product
# Create your views here.
def index(req):
    return render(req,"index.html")

def data(req):
    data=Product.objects.all()
    print(data)
    return render(req,"data.html",context={"data":data})

def insert(req):
    
    pname =  req.POST.get("product_name")
    pprice =  req.POST.get("product_price")
    
    if(pname or pprice):
        Product.objects.create(pname=pname,pprice=int(pprice))
        pname=""
        pprice=""
        
    
    return render(req,"insert.html",context={"data":{
        pname:pname,
        pprice:pprice
    }})