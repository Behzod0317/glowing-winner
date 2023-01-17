from .views import get_list,get_news,add_news
from django.urls import path

urlpatterns = [
    path('list/', get_list, ),
    path('get/<int:id>/',get_news),
    path('add/',add_news)
]