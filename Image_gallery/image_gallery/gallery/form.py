from django import forms
from .models import Category


#for category only one field is required
class CategoryForm(forms.Form):
    category_name = forms.CharField(max_length=50, help_text="enter a category name")


class ImageForm(forms.Form):
    image = forms.ImageField()
    title = forms.CharField(max_length=100)
    category = forms.ModelChoiceField(
            queryset=Category.objects.all(), empty_label='Select a Category')