
from django.urls import path, include
from .views import index, page0, page1, ForumView, ContentView, CategoryView


urlpatterns = [
    path('',index, name = 'index'),
    path('page1/', page1, name = 'page1'),
    path('page0/', page0, name = 'page0'), 
    path('<pk>/forum/', ForumView.as_view(), name='forum'),
    path('<pk>/content/', ContentView.as_view(), name='content'),
    path('categories/', CategoryView.as_view(), name='category'),
    

]


#if settings.DEBUG:
#    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
