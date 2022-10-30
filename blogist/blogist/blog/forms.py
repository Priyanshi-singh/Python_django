from socket import fromshare
from tkinter.tix import Form
from django import forms
from .models import Category, Image, Tag, Article

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('name',)

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image','caption')
    
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title','content','category','tags','status','duration')


