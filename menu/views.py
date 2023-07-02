from django.shortcuts import render
from django.views.generic import ListView
from .models import Category

def index(request):
    return render(  request, 'source.html', {'Title': 'pyreddit' }) 

class CategoryView(ListView):
    template_name = 'categories.html'
    model = Category

