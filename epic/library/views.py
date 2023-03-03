from django.shortcuts import render
from .models import Library
import os

def index(request):
    image = Library.objects.all()

    ctx={
        'images' : image,
        'title' : 'Library',
    }
    return render(request, 'index.html' , ctx)

