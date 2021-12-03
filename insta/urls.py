from django.urls import path
from .views import index, loginView, register

urlpatterns = [
    path('', index,name="index"),
    path('login/', loginView,name="login"),
    path('register/', register,name="register"),
]
