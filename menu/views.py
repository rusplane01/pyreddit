from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView
from .models import Category

def index(request):
    return render(  request, 'source.html', {'Title': 'pyshop' }, ) 

def page0(request):
    return render(  request, 'page0.html' )

def page1(request):
    return render(  request, 'page1.html' )


class ForumView(DetailView):
    template_name = 'menu/forum.html'
    model = Category
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(category = kwargs['object'])
        
        return context


class CategoryView(ListView):
    template_name = 'menu/categories.html'
    model = Category

    def get_context_data(self, **kwargs: any) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(category=kwargs['object'])

        return context

