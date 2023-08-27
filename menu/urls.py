from django.urls import path, include
from .views import index, page0, page1, ForumView


urlpatterns = [
    path('',index, name = 'index'),
    path('page1/', page1, name = 'page1'),
    path('page0/', page0, name = 'page0'), 
    path('<pk>/forum/', ForumView.as_view(), name='forum'),
    

]


#if settings.DEBUG:
#    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
