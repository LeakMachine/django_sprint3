# Generated by Django 3.2.16 on 2024-11-18 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20241119_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(auto_created=True, verbose_name='Добавлено'),
        ),
        migrations.AlterField(
            model_name='location',
            name='created_at',
            field=models.DateTimeField(auto_created=True, verbose_name='Добавлено'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_created=True, verbose_name='Добавлено'),
        ),
    ]
