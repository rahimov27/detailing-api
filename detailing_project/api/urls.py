# В файле api/urls.py
from django.urls import path
from .views import (
    MasterListCreateAPIView,
    MasterDetailAPIView,
    ClientListCreateAPIView,
    ClientDetailAPIView,
)

urlpatterns = [
    # URL для получения списка мастеров и создания нового мастера
    path("masters/", MasterListCreateAPIView.as_view(), name="master-list-create"),
    # URL для получения, обновления и удаления мастера по ID
    path("masters/<int:pk>/", MasterDetailAPIView.as_view(), name="master-detail"),
    # URL для получения списка клиентов и создания нового клиента
    path("clients/", ClientListCreateAPIView.as_view(), name="client-list-create"),
    # URL для получения, обновления и удаления клиента по ID
    path("clients/<int:pk>/", ClientDetailAPIView.as_view(), name="client-detail"),
]
