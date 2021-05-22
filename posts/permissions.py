from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsAuthorOrReadOnlyPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.author

    # def has_object_permission(self, request, view, obj):
    #     return bool(request.method in permissions.SAFE_METHODS or
    #                 request.user and request.user.is_authenticated and request.user == obj.author)