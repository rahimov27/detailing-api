from django.contrib import admin
from .models import Client, ApiKey


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "phone", "date")
    search_fields = ("first_name", "last_name", "phone", "date")


@admin.register(ApiKey)
class ApiKeyAdmin(admin.ModelAdmin):
    list_display = ("key", "created_at")
    search_fields = ("key",)
