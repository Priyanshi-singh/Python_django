from django.urls import path
from .views import *

urlpatterns = [
    path('',index, name = "index"),
     path('about/',about, name ='about'),
    path('view_image/<int:image_id>/', view_image, name='view_image'),
    path('cart/<int:product_id>/',cart, name='cart'),

]