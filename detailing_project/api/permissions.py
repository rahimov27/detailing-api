from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    """
    Разрешение для администраторов. Все остальные пользователи не могут выполнять действия.
    """

    def has_permission(self, request, view):
        # Проверяем, является ли пользователь администратором
        return request.user and request.user.is_staff
