from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet  # Asegúrate de importar tu PatientViewSet

router = DefaultRouter() # Crear un router
router.register(r'patients', PatientViewSet, basename='patients') # Registrar el PatientViewSet con el router

# Definir las URLs usando el router
urlpatterns = [
    path('api/', include(router.urls)),  # Incluir las rutas generadas por el router bajo /api/
]
