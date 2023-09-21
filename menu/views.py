from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView
from .models import Category, Product

def index(request):
    return render(  request, 'source.html', {'Title': 'pyshop' }, ) 

def page0(request):
    return render(  request, 'page0.html' )

def page1(request):
    return render(  request, 'page1.html' )


class ForumView(DetailView):
    template_name = 'forum.html'
    model = Category
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['object'] = Product.objects.filter(category = kwargs['object'])
        context_object_name = 'product'

        return context

class ContentView(DetailView):
    template_name = 'content.html'
    model = Product

class CategoryView(ListView):
    template_name = 'categories.html'
    model = Category

    def get_context_data(self, **kwargs: any) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        # context['products'] = Products.objects.filter(category=kwargs['categories'])

        return context

