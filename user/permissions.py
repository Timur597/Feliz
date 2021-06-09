from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import *


class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        try:
            request.user.is_superuser
        except:
            raise PermissionDenied('У вас нету прав доступа')
        return bool(request.user and request.user.is_superuser)


class IsSeller(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_seller)

