from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):  # пермишенс позволяют сделать так, тобы определенный юзер мог
    # изменить только свою запись, чужую может только читать
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


