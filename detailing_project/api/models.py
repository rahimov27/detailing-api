from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    STATUS_CHOICES = [
        ("pending", "Ожидание"),
        ("in_progress", "В работе"),
        ("completed", "Завершено"),
        ("cancelled", "Отменено"),
        ("unpaid", "Нет оплаты"),
    ]

    first_name = models.CharField(max_length=100, verbose_name="Имя", default="")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия", default="")
    phone = models.CharField(max_length=45, verbose_name="Телефон", default="")
    service = models.CharField(max_length=45, verbose_name="Услуга", default="")
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Цена услуги", default=0.00
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        verbose_name="Статус работы",
        default="pending",
    )
    date = models.DateTimeField(verbose_name="Дата создания", null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.service}"


class ApiKey(models.Model):
    key = models.CharField(max_length=64, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.key
