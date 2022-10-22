
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self) ->str:
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to ='images/')
    Category = models.ForeignKey(Category, on_delete = models.CASCADE)
    caption = models.CharField(max_length=40)
    created_at = models.DateField()

    def __str__(self) ->str:
        return self.caption

class Tag(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self) ->str:
        return self.name