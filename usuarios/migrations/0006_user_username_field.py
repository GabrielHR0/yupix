# Generated by Django 4.2.7 on 2023-12-17 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_remove_user_username_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='USERNAME_FIELD',
            field=models.CharField(default=models.CharField(max_length=50, verbose_name='Primeiro Nome'), max_length=50, verbose_name='Primeiro Nome'),
        ),
    ]
