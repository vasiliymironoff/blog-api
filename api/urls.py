from django.urls import path, include
from api import views

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth_token/', include('djoser.urls.authtoken')),
    path('posts/', views.PostListView.as_view()),
    path("post/", views.PostCreateView.as_view()),
    path('post/<int:pk>/', views.PostDetailView.as_view()),
    path('message/', views.MessageListView.as_view()),
    path('message/<int:pk>/', views.MessageDetailView.as_view()),
    path('user/', views.UserListView.as_view()),
    path('profile/<int:pk>/', views.UserDetailView.as_view()),
]
