from rest_framework import serializers
from api import models


class MessageSerializer(serializers.ModelSerializer):
    """Сезиалайзер сообщений"""
    class Meta:
        model = models.Message
        fields = '__all__'


class ProfileListSerializer(serializers.ModelSerializer):
    """Сериалайзер для списка всех пользователей"""
    username = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = models.Profile
        fields = ('id', "username", 'image')


class PostSerializer(serializers.ModelSerializer):
    """Сериалайзер постов с полной информацей"""
    author = ProfileListSerializer(many=False, read_only=True)

    class Meta:
        model = models.Post
        fields = '__all__'


class PostWithoutAuthorSerializer(serializers.ModelSerializer):
    """Сериализатор постов без автора для профиля"""

    class Meta:
        model = models.Post
        exclude = ('author',)


class ProfileDetailSerializer(serializers.ModelSerializer):
    """Сериалайзер с детальной информацией о пользователе + его посты"""
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.EmailField(source="user.email", read_only=True)
    posts = PostWithoutAuthorSerializer(read_only=True, many=True)

    class Meta:
        model = models.Profile
        fields = ("id", "username", "email", "status", "about", "birth_date", 'image', 'posts')


