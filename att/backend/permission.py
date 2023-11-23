from rest_framework.permissions import BasePermission


class HighPermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        print(f'user:{user}')
        if ("12" in str(user)):
            return True
        return False
