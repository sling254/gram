from django.urls import path, re_path
from .views import index, loginView, register, logoutuser, profileview,post,AddLike,AddDislike


urlpatterns = [
    path('', index,name="index"),
    path('login/', loginView,name="login"),
    path('register/', register,name="register"),
    path('logout/', logoutuser,name="logout"),
    path('profile/', profileview,name="profile"),
    path('post/', post,name="post"),
     path('post/<int:pk>/like', AddLike.as_view(), name='like'),
    path('post/<int:pk>/dislike', AddDislike.as_view(), name='dislike'),
    
    
]
