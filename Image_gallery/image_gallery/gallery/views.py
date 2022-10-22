from django.shortcuts import render,redirect
from .models import Category, Image
from .form import ImageForm, CategoryForm
import os

def index(request):
    #step 1 : load the data from database

    categories = Category.objects.all()  # to get all data 
    images = Image.objects.all()

    #step 2: pass the data into context

    ctx={
        'categories' : categories,
        'images' : images,
        'title' : 'Image Gallery',
    }

    #step 3: return the rendered templates

    return render(request, 'index.html' , ctx)

def add_category(request):
    form = CategoryForm()
    if request.method=="POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category=form.cleaned_data['category_name']
            category= Category(name=category)
            category.save()
            return redirect('index')
    ctx={
        'form': form,
        'category' : 'Add Category',
            
        }
    return render(request,'add_category.html',ctx)

def add_image(request): 

    form = ImageForm()  #it creates an empty form object
    
    if request.method=="POST":
        form=ImageForm(request.POST, request.FILES)
        if form.is_valid():
            title=form.cleaned_data['title']
            category=form.cleaned_data['category']
            image= form.cleaned_data['image']
            img=Image(title=title, category=category, image= image)
            img.save()
            return redirect('index')
    ctx={
        'form' : form,
        'title' : 'Add Image',
    }
    return render(request, 'add_image.html',ctx)

def view_image(request, image_id):
    try:
        item= Image.objects.get(id=image_id) 
        ctx = {
            'img' : item,
            'title' : item.title,
        }

        return render(request, 'index.html',ctx)
    except:
        return redirect('index')


def delete_image(request, image_id):
    try:
        item = Image.objects.get(id=image_id)   #get the image
        os.remove(item.image.path)              #delete the image file from media folder
        item.delete()                           #delete the image from database
    except:
        print('Error deleting image')
    return redirect('index')