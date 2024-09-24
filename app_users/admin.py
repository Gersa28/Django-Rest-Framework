from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Definir una clase personalizada para UserAdmin
class CustomUserAdmin(UserAdmin):
    # Agregar el campo 'groups' en la lista de columnas a mostrar
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_groups')

    # Método para mostrar los grupos
    def get_groups(self, obj):
        return ", ".join([group.name for group in obj.groups.all()])

    # Título de la columna
    get_groups.short_description = 'Groups'

# Desregistrar el UserAdmin por defecto y registrar el personalizado
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
