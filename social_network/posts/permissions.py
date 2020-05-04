from rest_framework import permissions


class ObjectAuthorPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if obj.author and request.user == obj.author:
            return True
        return False
