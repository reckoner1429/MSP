from django.urls import path
from .views import Login

urlpatterns = [
    path('login/', Login.as_view(), namespace="login"),
]