from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Client
from .serializers import ClientSerializer


class ClientListCreateAPIView(APIView):
    @swagger_auto_schema(
        operation_description="Получение списка клиентов",
        responses={
            200: openapi.Response(
                description="Список клиентов",
                schema=openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            "id": openapi.Schema(
                                type=openapi.TYPE_INTEGER, description="ID клиента"
                            ),
                            "first_name": openapi.Schema(
                                type=openapi.TYPE_STRING, description="Имя клиента"
                            ),
                            "last_name": openapi.Schema(
                                type=openapi.TYPE_STRING, description="Фамилия клиента"
                            ),
                            "email": openapi.Schema(
                                type=openapi.TYPE_STRING, description="Email клиента"
                            ),
                            "phone": openapi.Schema(
                                type=openapi.TYPE_STRING, description="Телефон клиента"
                            ),
                        },
                    ),
                ),
            )
        },
    )
    def get(self, request):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Создание нового клиента",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "first_name": openapi.Schema(
                    type=openapi.TYPE_STRING, description="Имя клиента"
                ),
                "last_name": openapi.Schema(
                    type=openapi.TYPE_STRING, description="Фамилия клиента"
                ),
                "email": openapi.Schema(
                    type=openapi.TYPE_STRING, description="Email клиента"
                ),
                "phone": openapi.Schema(
                    type=openapi.TYPE_STRING, description="Телефон клиента"
                ),
            },
            required=["first_name", "last_name", "email", "phone"],
        ),
        responses={201: openapi.Response("Клиент создан")},
    )
    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
