from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')
    avatar = models.ImageField(upload_to='user/', verbose_name='Аватар', **NULLABLE)
    phone = models.CharField(max_length=20, verbose_name='Телефон', **NULLABLE)
    town = models.CharField(max_length=20, verbose_name='Город', **NULLABLE)
    telegram_id = models.CharField(max_length=100, verbose_name='Телеграмм', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
