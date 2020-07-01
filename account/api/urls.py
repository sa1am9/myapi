from django.urls import path
from .views import registration_view, all_posts, UserLoginView

urlpatterns = [
    path('register/', registration_view),
    path('all/', all_posts),
    path('login/', UserLoginView.as_view())
]