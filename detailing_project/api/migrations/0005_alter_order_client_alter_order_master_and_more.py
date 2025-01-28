# Generated by Django 5.1.5 on 2025-01-26 21:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_master_remove_client_email_order_master'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.client', verbose_name='Клиент'),
        ),
        migrations.AlterField(
            model_name='order',
            name='master',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.master', verbose_name='Мастер'),
        ),
        migrations.AlterField(
            model_name='order',
            name='notes',
            field=models.TextField(blank=True, verbose_name='Примечания'),
        ),
        migrations.AlterField(
            model_name='order',
            name='services',
            field=models.ManyToManyField(to='api.service', verbose_name='Услуги'),
        ),
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Стоимость'),
        ),
    ]
