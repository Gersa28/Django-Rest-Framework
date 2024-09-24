from rest_framework import permissions


class IsDoctor(permissions.BasePermission):
    def has_permission(self, request, view): # Returns True or False
        return request.user.groups.filter(name='doctors').exists() # El objeto user es el objeto básico de Django, el usuario tiene dato del grupo al que pertenece