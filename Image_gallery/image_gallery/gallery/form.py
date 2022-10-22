from django import forms

#for category only one field is required
class CategoryForm(forms.Form):
    name = forms.CharField(max_length=50, help_text="enter a category name")


class ImageForm(forms.Form):
    image = forms.ImageField()
    title = forms.CharField(max_length=100)
    category = forms.CharField(max_length =50)