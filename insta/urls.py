from django.urls import path, re_path
from .views import index, loginView, register, logoutuser, post,AddLike,AddDislike,ProfileView,ProfileEditView,PostDetailView,PostEditView,PostDeleteView,CommentDeleteView,AddFollower,RemoveFollower


urlpatterns = [
    path('', index,name="index"),
    path('login/', loginView,name="login"),
    path('register/', register,name="register"),
    path('logout/', logoutuser,name="logout"),
    path('profile/<int:pk>/', ProfileView.as_view(),name="profile"),
    path('profile/edit/<int:pk>/', ProfileEditView.as_view(), name='profile-edit'),
    path('post/', post,name="post"),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/edit/<int:pk>/', PostEditView.as_view(), name='post-edit'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:post_pk>/comment/delete/<int:pk>/', CommentDeleteView.as_view(), name='comment-delete'),
    path('post/<int:pk>/like', AddLike.as_view(), name='like'),
    path('post/<int:pk>/dislike', AddDislike.as_view(), name='dislike'),
    path('profile/<int:pk>/followers/add', AddFollower.as_view(), name='add-follower'),
     
    path('profile/<int:pk>/followers/remove', RemoveFollower.as_view(), name='remove-follower'),
    
    
]
