# Generated by Django 3.2.6 on 2022-01-17 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0006_rename_загрузка cpu_cpu_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cpu',
            name='number',
        ),
        migrations.AddField(
            model_name='cpu',
            name='Загрузка CPU',
            field=models.FloatField(null=True),
        ),
    ]