from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    """Модель пользователя"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    image = models.ImageField("Фото пользователя", null=True, blank=True, default="")
    about = models.CharField('Краткая информация', max_length=400, null=True, blank=True, default="")
    status = models.CharField('Статус', max_length=40, null=True, blank=True, default="")
    birth_date = models.DateTimeField(null=True, blank=True)
    is_men = models.BooleanField(null=True, blank=True, default=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
        ordering = ["-id"]


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Post(models.Model):
    """Пост"""
    author = models.ForeignKey(Profile, verbose_name='Автор', on_delete=models.CASCADE, related_name='posts')
    title = models.CharField("Заголовок", max_length=100, null=True)
    text = models.TextField("Текст")
    time = models.DateTimeField("Время", auto_now=True)

    def __str__(self):
        return str(self.pk) + " " + self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-time']


class Message(models.Model):
    """Сообщение"""
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='send')
    recipient = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='received')
    text = models.TextField("Сообщение", null=True, blank=True, default="")
    image = models.ImageField("Фото", null=True, blank=True, default="")
    time = models.DateTimeField("Время", auto_now_add=True)

    def __str__(self):
        return str(self.sender) + " - " + str(self.recipient)

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
