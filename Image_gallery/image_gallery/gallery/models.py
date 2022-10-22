from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    uploaded_at = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title
