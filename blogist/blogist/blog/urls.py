from django.urls import path
from .views import *

urlpatterns = [
    path('', landing, name='landing'),
    path('home/', index, name='home'),
    path('article/new/', article_create, name='create'),
]