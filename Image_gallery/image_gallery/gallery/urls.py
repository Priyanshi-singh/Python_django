from importlib.resources import path
from .views import *
from django.urls import path

urlpatterns = [
    #path_inline
    path('', index, name='index'),
    path('add_category/', add_category, name='add_category'),
    path('add_image/', add_image, name='add_image'),
    #dynamic urls
    path('view_image/<int:image_id>/', view_image, name='view_image'),
    path('delete_image/<int:image_id>/', delete_image, name='delete_image'),
]