from django.urls import path, include
from .views import registration_view, all, UserLoginView

urlpatterns=[
    path('register/', registration_view),
    path('all/', all),
    path('login/', UserLoginView.as_view())
]