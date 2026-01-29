from rest_framework import permissions



class CheckRole(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'seller'


class CheckOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'buyer'