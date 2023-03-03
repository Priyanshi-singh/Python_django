from django.contrib import admin
from .models import *

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title','image')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

