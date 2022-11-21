from rest_framework.permissions import SAFE_METHODS, BasePermission

from reviews.models import ADMIN_ROLE, MODERATOR_ROLE


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return (request.method in SAFE_METHODS
                or (request.user.is_authenticated
                    and (request.user.role == ADMIN_ROLE
                         or request.user.is_superuser)))


class IsAuthorOrModeratorOrAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return (request.method in SAFE_METHODS
                or request.user == obj.author
                or request.user.role == MODERATOR_ROLE
                or request.user.role == ADMIN_ROLE
                or request.user.is_superuser)


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return not request.user.is_anonymous and (
                request.user.role == ADMIN_ROLE
                or request.user.is_superuser)

    def has_object_permission(self, request, view, obj):
        return not request.user.is_anonymous and (
                request.user.role == ADMIN_ROLE
                or request.user.is_superuser)
