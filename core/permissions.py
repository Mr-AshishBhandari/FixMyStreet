from rest_framework.permissions import BasePermission, SAFE_METHODS


class UpdateByAdminOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in ("GET", "HEAD", "OPTIONS", "POST"):
            return True
        return bool(request.user and request.user.is_staff)
