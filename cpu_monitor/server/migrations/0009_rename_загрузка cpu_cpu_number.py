# Generated by Django 3.2.6 on 2022-01-17 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0008_alter_cpu_загрузка cpu'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cpu',
            old_name='Загрузка CPU',
            new_name='number',
        ),
    ]
