from django.contrib import admin
from .models import Client, Service, Order


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "email",
        "phone",
    )
    search_fields = ("first_name", "last_name", "email")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "price")
    search_fields = ("name",)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "client", "status")
    list_filter = ("status",)
    search_fields = ("client__first_name", "client__last_name")
