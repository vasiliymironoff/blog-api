# Generated by Django 3.2.3 on 2021-05-17 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Профиль', 'verbose_name_plural': 'Профили'},
        ),
        migrations.RemoveField(
            model_name='message',
            name='edit',
        ),
    ]
