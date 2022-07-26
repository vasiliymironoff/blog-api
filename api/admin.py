from django.contrib import admin
from . import models


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time')


class MessageAdmin(admin.ModelAdmin):
    list_display = ("sender", "recipient", 'time')


admin.site.register(models.Profile)
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Message, MessageAdmin)
