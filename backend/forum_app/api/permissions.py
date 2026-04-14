from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsOwnerOrReadOnly(BasePermission):
    """Allow write actions only for the object owner or admin users."""

    def has_object_permission(self, request, view, obj):
        """Check whether the user may access or modify the object."""

        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user or request.user.is_superuser