from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    photo = models.ImageField(upload_to="user_photos/", null=True, blank=True)
    phone_number = models.CharField(max_length=13, unique=True, null=True, blank=True)

    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name='custom_user_set',  # Specify unique related name
        related_query_name='group',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='custom_user_set',  # Specify unique related name
        related_query_name='permission',
    )

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
