from django.http import JsonResponse
from .models import ApiKey


class ApiKeyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith("/api/"):  # Ограничиваем только API-запросы
            api_key = request.headers.get("Authorization")
            if (
                not api_key
                or not ApiKey.objects.filter(
                    key=api_key.replace("Api-Key ", "")
                ).exists()
            ):
                return JsonResponse({"error": "Invalid API key"}, status=403)
        return self.get_response(request)
