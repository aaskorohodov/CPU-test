from django.db import models


class CPU(models.Model):
    number = models.FloatField(unique=False)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
