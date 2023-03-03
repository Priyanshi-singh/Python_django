from django.shortcuts import render
from .models import Library
import os

def index(request):
    images = Library.objects.all()

    ctx={
        'images' : images,
        'title' : 'Library',
    }
    return render(request, 'index.html' , ctx)

