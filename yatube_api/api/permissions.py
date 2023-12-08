from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied


class AuthorOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if (request.method in permissions.SAFE_METHODS
                or obj.author == request.user):
            return True


class GroupOnlyGet(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return request.user
        raise PermissionDenied()
