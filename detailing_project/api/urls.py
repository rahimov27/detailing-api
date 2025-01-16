from django.urls import path
from .views import ClientListCreateAPIView

urlpatterns = [
    path("clients/", ClientListCreateAPIView.as_view(), name="client-list-create"),
]
