from django.contrib import admin
from .models import Client, Service, Order, Master


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "phone",
    )
    search_fields = ("first_name", "last_name", "phone")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "price")
    search_fields = ("name",)


@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "specialization")
    search_fields = ("first_name", "last_name", "specialization")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "client", "master", "status")
    list_filter = ("status", "master")
    search_fields = (
        "client__first_name",
        "client__last_name",
        "master__first_name",
        "master__last_name",
    )
