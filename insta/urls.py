from django.urls import path, re_path
from .views import index, loginView, register, logoutuser, post,AddLike,AddDislike,ProfileView,ProfileEditView


urlpatterns = [
    path('', index,name="index"),
    path('login/', loginView,name="login"),
    path('register/', register,name="register"),
    path('logout/', logoutuser,name="logout"),
    path('profile/<int:pk>/', ProfileView.as_view(),name="profile"),
    path('profile/edit/<int:pk>/', ProfileEditView.as_view(), name='profile-edit'),
    path('post/', post,name="post"),
    path('post/<int:pk>/like', AddLike.as_view(), name='like'),
    path('post/<int:pk>/dislike', AddDislike.as_view(), name='dislike'),
    
    
]
