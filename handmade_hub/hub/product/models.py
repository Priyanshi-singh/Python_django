from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.name

class Image(models.Model):
    title = models.CharField(max_length=40)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=200)
    uploaded_at = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

    def __str__(self):
       return self.title
