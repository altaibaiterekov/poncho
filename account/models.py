from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    nickname = models.CharField(max_length=100, blank=True)
    avatar = models.ImageField(upload_to='avatars', blank=True, default='avatars/default_avatar.jpg')

    def __str__(self):
        return f'{self.email}'
