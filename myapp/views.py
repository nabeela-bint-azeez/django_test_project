from django.shortcuts import render,redirect
from .forms import ProductForm
from .models import Product
# Create your views here.

def add_product(request):
    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form=ProductForm()
    return render(request,'add_product.html',{'form':form})


def product_list(request):
    products=Product.objects.all()
    return render(request,'product_list.html',{'products':products})

def update_product(request,pk):
    products=Product.objects.get(id=pk)
    form=ProductForm(request.POST or None,instance=products)   
    if request.method=='POST':
        if form.is_valid():
            form.save()
            return redirect('list')
    return render(request,'add_product.html',{'form':form})

def delete_product(request,pk):
    products=Product.objects.get(id=pk)
    products.delete()
    return redirect('list')