# В файле api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Master, Client
from .serializers import MasterSerializer, ClientSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class MasterListCreateAPIView(APIView):
    @swagger_auto_schema(
        operation_description="Получение списка мастеров и создание нового мастера.",
        responses={200: MasterSerializer(many=True), 201: "Мастер создан"},
    )
    def get(self, request):
        masters = Master.objects.all()
        serializer = MasterSerializer(masters, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MasterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MasterDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            master = Master.objects.get(pk=pk)
        except Master.DoesNotExist:
            return Response(
                {"detail": "Мастер не найден"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = MasterSerializer(master)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            master = Master.objects.get(pk=pk)
        except Master.DoesNotExist:
            return Response(
                {"detail": "Мастер не найден"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = MasterSerializer(master, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            master = Master.objects.get(pk=pk)
        except Master.DoesNotExist:
            return Response(
                {"detail": "Мастер не найден"}, status=status.HTTP_404_NOT_FOUND
            )
        master.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ClientListCreateAPIView(APIView):
    @swagger_auto_schema(
        operation_description="Получение списка клиентов и создание нового клиента.",
        responses={200: ClientSerializer(many=True), 201: "Клиент создан"},
        request_body=ClientSerializer,  # ✅ Добавляем тело запроса
    )
    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)


class ClientDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            client = Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            return Response(
                {"detail": "Клиент не найден"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = ClientSerializer(client)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            client = Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            return Response(
                {"detail": "Клиент не найден"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            client = Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            return Response(
                {"detail": "Клиент не найден"}, status=status.HTTP_404_NOT_FOUND
            )
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
