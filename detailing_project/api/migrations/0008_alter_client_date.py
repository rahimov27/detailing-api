# Generated by Django 5.1.5 on 2025-01-28 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_client_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
    ]
