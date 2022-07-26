from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers
from api import models

DATETIME_FORMAT = '%H:%M %d.%m.%Y'


class ProfileListSerializer(serializers.ModelSerializer):
    """Сериалайзер для списка всех пользователей"""
    username = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = models.Profile
        fields = ('id', "username", 'image')


class PostSerializer(serializers.ModelSerializer):
    """Сериалайзер постов с полной информацей"""
    author = ProfileListSerializer(many=False, read_only=True)
    time = serializers.DateTimeField(format=DATETIME_FORMAT, read_only=True)

    class Meta:
        model = models.Post
        fields = ("id", "author", 'text', 'title', 'time')


class PostCreateSerializer(serializers.ModelSerializer):
    """Сериалайзер постов для создания"""

    time = serializers.DateTimeField(format=DATETIME_FORMAT, read_only=True)
    title = serializers.CharField(max_length=100, required=False)

    class Meta:
        model = models.Post
        fields = ("author", 'text', 'title', 'time')


class PostWithoutAuthorSerializer(serializers.ModelSerializer):
    """Сериализатор постов без автора для профиля"""
    time = serializers.DateTimeField(format=DATETIME_FORMAT, read_only=True)

    class Meta:
        model = models.Post
        exclude = ('author',)


class ProfileDetailSerializer(serializers.ModelSerializer):
    """Сериалайзер с детальной информацией о пользователе + его посты"""
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.EmailField(source="user.email", read_only=True)
    posts = PostWithoutAuthorSerializer(read_only=True, many=True)
    id = serializers.IntegerField(read_only=True)
    image = Base64ImageField(required=False)

    class Meta:
        model = models.Profile
        fields = ("status",
                  "about",
                  'image',
                  'is_men',
                  "username",
                  "email",
                  "posts",
                  "id")


class MessageSerializer(serializers.ModelSerializer):
    """Сезиалайзер сообщений"""
    image = Base64ImageField(required=False)
    text = serializers.CharField(required=False)
    time = serializers.DateTimeField(format=DATETIME_FORMAT, read_only=True)

    class Meta:
        model = models.Message
        fields = ("id",
                  "text",
                  "image",
                  "time",
                  "sender",
                  "recipient")
