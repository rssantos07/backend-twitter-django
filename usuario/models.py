from django.db import models
from django.http import HttpRequest
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from rest_framework.response import Response
from rest_framework import status


class User(AbstractUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self) -> str:
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=300)
    bio = models.CharField(max_length=300)
    image = models.ImageField(default="default.jpg",
                              upload_to="media/user_images/", null=True, blank=True)
    verified = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.full_name


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mensagem = models.TextField()
    imagem = models.ImageField(upload_to='media/posts/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def formatted_created_at(self):
        return self.created_at.strftime("%d/%m/%Y %H:%M")

    def __str__(self):
        return self.mensagem[:20]


def create(self, validated_data):
        user = self.context['request'].user  # Obtém o usuário da solicitação
        post = Post.objects.create(user=user, **validated_data)
        return post