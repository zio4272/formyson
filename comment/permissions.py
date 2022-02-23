from rest_framework.permissions import BasePermission, IsAdminUser

class IsUser(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

class IsSuperUser(IsAdminUser):
    def has_object_permission(self, request, view, obj):
        print(request, obj)
        return obj.user == request.user