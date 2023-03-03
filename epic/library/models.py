from django.db import models

class Library(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=30)
    uploaded_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

