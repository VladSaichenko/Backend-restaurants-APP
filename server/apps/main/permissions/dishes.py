from rest_framework import permissions


class AuthenticatedCreateOnlyDish(permissions.BasePermission):
    message = 'You can send only GET and POST!'

    def has_permission(self, request, view):
        if request.method == 'POST':
            return request.user.is_authenticated
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return False
