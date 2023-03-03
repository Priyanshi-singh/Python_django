from django.contrib import admin
from .models import Library

@admin.register(Library)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title','image')
   
    