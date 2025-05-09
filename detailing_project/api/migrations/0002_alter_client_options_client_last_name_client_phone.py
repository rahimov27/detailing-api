# Generated by Django 5.1.5 on 2025-01-15 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name': 'Клиент', 'verbose_name_plural': 'Клиенты'},
        ),
        migrations.AddField(
            model_name='client',
            name='last_name',
            field=models.CharField(default='', max_length=100, verbose_name='Фамилия'),
        ),
        migrations.AddField(
            model_name='client',
            name='phone',
            field=models.CharField(default='', max_length=15, verbose_name='Телефон'),
        ),
    ]
