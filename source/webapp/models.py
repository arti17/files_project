from django.contrib.auth.models import User
from django.db import models


class File(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    author = models.ForeignKey(User, null=True, blank=True, related_name='files', on_delete=models.CASCADE, verbose_name='Автор')
