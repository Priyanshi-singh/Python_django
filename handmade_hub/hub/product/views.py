from django.shortcuts import render, redirect, get_object_or_404
from .models import *

def index(request):
    image = Image.objects.all()

    ctx={
        'images' : image,
        'title' : 'Handmade Hub',
    }
    return render(request, 'product/index.html' , ctx)

def view_image(request, image_id):
    try:
        item= Image.objects.get(id=image_id) 
        ctx = {
            'img' : item,
            'title' : item.title,
        }

        return render(request, 'product/image_view.html',ctx)
    except:
        return redirect('index')

def cart(request,product_id):
    try:
        item=Image.objects.get(id=product_id)
        ctx={
            'product': item,
            'title' : 'Cart'
        }

        return render(request, 'product/cart.html')
    except:
        return redirect('index')

def about(request):
    return render(request,'product/about.html')