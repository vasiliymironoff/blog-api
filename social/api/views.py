from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response
from social_core.pipeline import user

from api.serializers import *
from api import models
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from django.contrib.auth import get_user_model
# Create your views here.


class PostListView(generics.ListAPIView):
    """cписок всех постов или отдельного автора"""
    serializer_class = PostSerializer

    def get_queryset(self):
        result = models.Post.objects.all()
        if self.request.query_params.get('author', None) is not None:
            result = models.Post.objects.filter(author=models.Profile.objects.get(pk=self.request.query_params.get('author', None)))
        return result


class PostCreateView(generics.CreateAPIView):
    serializer_class = PostCreateSerializer
    queryset = models.Post.objects.all()


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Создание, обновление и удаление поста"""
    serializer_class = PostSerializer
    queryset = models.Post.objects.all()


class MessageListView(generics.ListCreateAPIView):
    """Список сообщений отдельной пересписки 2 людей и создание """
    serializer_class = MessageSerializer

    def get_queryset(self):
        if (self.request.query_params.get('user1', None) is not None
                and self.request.query_params.get('user2', None) is not None):
            result = models.Message.objects.filter(sender=self.request.query_params.get('user1', None),
                                                   recipient=self.request.query_params.get('user2', None))
            result = result.union(models.Message.objects.filter(sender=self.request.query_params.get('user2', None),
                                                                recipient=self.request.query_params.get('user1', None)))
            return result

    def post(self, request, *args, **kwargs):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)


class MessageDetailView(generics.RetrieveUpdateDestroyAPIView):
    """обновление, удаление сообщения"""
    serializer_class = MessageSerializer
    queryset = models.Message.objects.all()


class UserListView(generics.ListAPIView):
    queryset = models.Profile.objects.all()
    serializer_class = ProfileListSerializer


class UserDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileDetailSerializer

    def get_queryset(self):
        return models.Profile.objects.all()


