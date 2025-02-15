from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Client, ApiKey
from .serializers import ClientSerializer
from drf_yasg.utils import swagger_auto_schema
from django.http import HttpResponse
import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A3
from reportlab.lib import colors
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics  # ✅ Импортируем pdfmetrics


# Функция для обрезки текста с добавлением многоточия
def truncate_text(text, max_length):
    if len(text) > max_length:
        return text[:max_length] + "..."
    return text


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


from reportlab.lib.pagesizes import A3
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import os
from datetime import datetime


from datetime import datetime
from django.db.models import Q


class ClientReportPDFAPIView(APIView):
    def get(self, request):
        # Получаем API ключ
        api_key = request.headers.get("Authorization")

        # Проверка API-ключа
        if not api_key or not ApiKey.objects.filter(key=api_key).exists():
            return Response(
                {"error": "Invalid API key"}, status=status.HTTP_403_FORBIDDEN
            )

        # Получаем параметры для фильтрации (месяц и год)
        month = request.query_params.get("month")
        year = request.query_params.get("year")

        # Проверка наличия месяцев и года
        if not month or not year:
            return Response(
                {"error": "Month and year parameters are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Преобразуем месяц и год в целые числа
        try:
            month = int(month)
            year = int(year)
        except ValueError:
            return Response(
                {"error": "Invalid month or year format"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Фильтрация клиентов по месяцу и году
        clients = Client.objects.filter(Q(date__month=month) & Q(date__year=year))

        # Продолжаем создание PDF
        response = HttpResponse(content_type="application/pdf")
        response["Content-Disposition"] = 'attachment; filename="client_report.pdf"'

        p = canvas.Canvas(response, pagesize=A3)
        width, height = A3
        y_position = height - 50

        font_path = "/Users/r27/Downloads/djsans/DejaVuSans.ttf"
        if not os.path.exists(font_path):
            return Response(
                {"error": "Font file not found"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        pdfmetrics.registerFont(TTFont("DejaVu", font_path))

        # Заголовок (увеличенный шрифт)
        p.setFont("DejaVu", 16)
        p.setFillColor(colors.black)
        p.drawString(60, y_position, "ОТЧЕТ")
        y_position -= 30

        # Черные линии по бокам
        p.setFillColor(colors.black)
        p.rect(20, 40, width - 60, height - 100, fill=0)

        # Добавляем дату и название компании
        company_name = "A1-workspace"
        current_month = datetime(year, month, 1).strftime("%B %Y")
        p.setFont("DejaVu", 12)
        p.drawString(60, height - 20, f"{company_name} - Отчет за {current_month}")

        # Подписи столбцов
        columns = ["ФИО", "Телефон", "Услуга", "Цена (KGS)", "Статус", "Дата"]
        x_positions = [60, 200, 350, 470, 580, 680]

        p.setFont("DejaVu", 12)
        for i, col in enumerate(columns):
            p.drawString(x_positions[i], y_position, col)
        y_position -= 10
        p.line(20, y_position, width - 40, y_position)
        y_position -= 20

        # Данные клиентов
        total_income = 0
        p.setFont("DejaVu", 10)
        for client in clients:
            name = f"{client.first_name} {client.last_name}"
            truncated_name = truncate_text(name, 12)

            data = [
                truncated_name,
                client.phone,
                client.service,
                f"{client.price} KGS",
                client.status,
                client.date.strftime("%d.%m.%Y") if client.date else "Не указано",
            ]

            for i, value in enumerate(data):
                p.drawString(x_positions[i], y_position, str(value))
            y_position -= 20

            total_income += client.price

            if y_position < 50:
                p.showPage()
                p.setFont("DejaVu", 10)
                y_position = height - 50

        p.showPage()
        p.save()
        return response
