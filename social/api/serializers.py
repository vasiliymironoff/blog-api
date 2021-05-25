import drf_extra_fields.fields
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
        fields = ("author", 'text', 'title', 'time')


class PostCreateSerializer(serializers.ModelSerializer):
    """Сериалайзер постов для создания"""

    time = serializers.DateTimeField(format=DATETIME_FORMAT, read_only=True)

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
    image = Base64ImageField()

    class Meta:
        model = models.Profile
        fields = ("status",
                  "about",
                  "birth_date",
                  'image',
                  'is_men',
                  "username",
                  "email",
                  "posts",
                  "id")

    def create(self, validated_data):
        image = validated_data.pop('image')
        status = validated_data.pop("status")
        about = validated_data.pop("about")
        is_men = validated_data.pop("is_men")
        birth_date = validated_data.pop("birth_date")

        return ProfileDetailSerializer.objects.create(image=image,
                                                      status=status,
                                                      about=about,
                                                      is_men=is_men,
                                                      birth_date=birth_date
                                                      )


class MessageSerializer(serializers.ModelSerializer):
    """Сезиалайзер сообщений"""
    image = Base64ImageField(required=False)
    time = serializers.DateTimeField(format=DATETIME_FORMAT, read_only=True)

    class Meta:
        model = models.Message
        fields = ("id",
                  "text",
                  "image",
                  "time",
                  "sender",
                  "recipient")

    def create(self, validated_data):
        text = validated_data.pop("text")
        sender = validated_data.pop("sender")
        recipient = validated_data.pop("recipient")
        try:
            image = validated_data.pop("image")
            return models.Message.objects.create(text=text,
                                                 image=image,
                                                 sender=sender,
                                                 recipient=recipient)
        except:
            return models.Message.objects.create(text=text,
                                                 sender=sender,
                                                 recipient=recipient)
