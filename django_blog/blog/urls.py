from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register_view, profile_view, home
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, CommentUpdateView, CommentDeleteView,CommentCreateView, PostByTagListView, PostSearchView

urlpatterns = [
    path('', home, name='home'),
    path('register/', register_view, name='register'),
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='blog/logged_out.html'), name='logout'),
    path('profile/', profile_view, name='profile'),
    
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    
    path('post/<int:pk>/comments/new/',CommentCreateView.as_view(), name='add-comment'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/',CommentDeleteView.as_view(), name='comment-delete'),
    
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts-by-tag'),
     path('search/', PostSearchView.as_view(), name='post-search'),

    
]
