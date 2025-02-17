# В файле api/urls.py
from django.urls import path
from .views import (
    ClientListCreateAPIView,
    ClientDetailAPIView,
    ClientReportPDFAPIView,
)

urlpatterns = [
    path("clients/", ClientListCreateAPIView.as_view(), name="client-list-create"),
    path("clients/<int:pk>/", ClientDetailAPIView.as_view(), name="client-detail"),
    path("report/", ClientReportPDFAPIView.as_view(), name="report"),
]
