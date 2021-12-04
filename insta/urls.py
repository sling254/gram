from django.urls import path
from .views import index, loginView, register, logoutuser, profileview
urlpatterns = [
    path('', index,name="index"),
    path('login/', loginView,name="login"),
    path('register/', register,name="register"),
    path('logout/', logoutuser,name="logout"),
    path('profile/', profileview,name="profile"),
]
