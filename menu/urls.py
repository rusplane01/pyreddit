from django.urls import path, include
from .views import index, page0, CategoryView


urlpatterns = [
    path('',index),
    path('page1/', CategoryView.as_view()),
    path('page0/', page0),
    

]


#if settings.DEBUG:
#    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
