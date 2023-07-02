from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True) # уникуе
    def __str__(self):
        return f'{self.name}'

    
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True) 
    category = models.ForeignKey(Category, on_delete=models.CASCADE) 
    image = models.ImageField(upload_to='posts/', null=True, blank=True) 
    def __str__(self):
        return f'{self.title}'