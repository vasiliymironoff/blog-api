from django.contrib import admin
from django.urls import path, include
from api import views

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth_token/', include('djoser.urls.authtoken')),
    # ?author=
    path('post/', views.PostListView.as_view()),
    path('post/<int:pk>/', views.PostDetailView.as_view()),
    # ?user1=N & user2=N
    path('message/', views.MessageListView.as_view()),
    path('message/<int:pk>/', views.MessageDetailView.as_view()),
    path('user/', views.UserListView.as_view()),
    path('profile/<int:pk>/', views.UserDetailView.as_view()),

]
