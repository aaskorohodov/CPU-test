# Generated by Django 3.2.6 on 2022-01-17 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0004_alter_cpu_загрузка cpu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpu',
            name='Загрузка CPU',
            field=models.PositiveIntegerField(),
        ),
    ]
