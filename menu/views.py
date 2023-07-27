from django.shortcuts import render
from django.views.generic import ListView
from .models import Category

def index(request):
    return render(  request, 'source.html', {'Title': 'pyshop' }, ) 

def page0(request):
    return render(  request, 'page0.html' )

class CategoryView(ListView):
    template_name = 'page1.html'
    
    model = Category

