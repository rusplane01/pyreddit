from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Category, Post

def index(request):
    return render(  request, 'menu/source.html', {'Title': 'pyreddit' }) 


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

