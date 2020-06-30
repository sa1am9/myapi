
from django.urls import path, include
from .views import post_element, post_collection, like_post, unlike_post, analitics
urlpatterns = [
    # api
    path('posts/', post_collection),
    path('post/<int:pk>', post_element),
    path('post/<int:pk>/like', like_post),
    path('post/<int:pk>/unlike', unlike_post),
    path('posts/analitics', analitics)
]