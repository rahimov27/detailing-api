# В файле detailing_project/urls.py
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin
from api.views import HomeMessage, Support

# Создание схемы для Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="CRM Detailing API",
        default_version="v1",
        description="Документация для API по управлению детейлингом",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# Маршруты
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomeMessage.as_view()),
    path("api/", include("api.urls")),  # Подключаем маршруты из api/urls.py
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="swagger-schema",
    ),
    path("support/", Support.as_view()),
]
