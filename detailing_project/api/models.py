from django.db import models
from django.contrib.auth.models import User


# Модель мастера
class Master(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Имя", default="")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия", default="")
    specialization = models.CharField(
        max_length=200, verbose_name="Специализация", default=""
    )

    class Meta:
        verbose_name = "Мастер"
        verbose_name_plural = "Мастера"

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.specialization})"


# Модель клиента
class Client(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Имя", default="")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия", default="")
    phone = models.CharField(max_length=15, verbose_name="Телефон", default="")
    service = models.CharField(max_length=40, verbose_name="Услуга", default="")
    date = models.DateTimeField(verbose_name="Дата создания", null=True, blank=True)

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# Модель услуги
class Service(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название услуги", default="")
    description = models.TextField(blank=True, verbose_name="Описание", default="")
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Стоимость", default=0.0
    )

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return self.name


# Модель заказа
class Order(models.Model):
    STATUS_CHOICES = [
        ("pending", "Ожидание"),
        ("in_progress", "В процессе"),
        ("completed", "Завершено"),
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Клиент")
    services = models.ManyToManyField(Service, verbose_name="Услуги")
    master = models.ForeignKey(
        Master, on_delete=models.CASCADE, verbose_name="Мастер"
    )  # Ссылка на мастера
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="pending", verbose_name="Статус"
    )
    notes = models.TextField(blank=True, verbose_name="Примечания")

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f"Заказ #{self.id} - {self.client} ({self.master})"
