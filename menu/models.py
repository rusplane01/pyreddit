from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True) # уникуе
    def __str__(self):
        return f'{self.name}'

    
class Product(models.Model):
    title = models.CharField(max_length=23)
    description = models.CharField(null=True, blank=True, max_length=60)
    price = models.CharField(null=False, blank=True, max_length=3) 
    category = models.ForeignKey(Category, on_delete=models.CASCADE) 
    image = models.ImageField(upload_to='objects/', null=True, blank=True) 
    def __str__(self):
        return f'{self.title}'