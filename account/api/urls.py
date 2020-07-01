from django.urls import path
from .views import registration_view, all_account, UserLoginView

urlpatterns = [
    path('register/', registration_view),
    path('all/', all_account),
    path('login/', UserLoginView.as_view())
]