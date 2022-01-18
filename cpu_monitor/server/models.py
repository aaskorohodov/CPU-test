from django.db import models


class CPU(models.Model):
    '''Модель хранит измерения загрузки CPU. Имена полей наглядно демонстрируют что:
    number = сама загрузка
    time_create = время измерения'''
    number = models.FloatField(unique=False)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
