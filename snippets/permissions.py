from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    # code snippet의 owner 만 수정할 수 있게 하는 Custom permission 이다
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.owner == request.user