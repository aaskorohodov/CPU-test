# Generated by Django 3.2.6 on 2022-01-17 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0009_rename_загрузка cpu_cpu_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpu',
            name='number',
            field=models.FloatField(),
        ),
    ]