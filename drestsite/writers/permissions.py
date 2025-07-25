from rest_framework import permissions

class IsAdminUserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return bool(request.user and request.user.is_staff)
    

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print(f"User: {request.user}")
        print(f"Object owner: {obj.user}")
        print(f"Method: {request.method}")
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user

