from django.urls import path
from .views import index, CategoryView, ForumView

urlpatterns = [
    path('', index),
    path('categories/', CategoryView.as_view(), name = 'category'),
    path('<pk>/forum/', ForumView.as_view(), name = 'forum')
]
 