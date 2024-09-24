from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app_patients.views import PatientViewSet  # Asegúrate de importar correctamente tu PatientViewSet
from app_doctors.viewsets import DoctorViewSet  
from app_doctors.viewsets import ListDepartmentViewSet  
from app_doctors.viewsets import ListDoctorAvailabilityViewSet  
from app_doctors.viewsets import ListMedicalNoteViewSet  as ListMedicalNoteViewSetMedical
from app_bookings.views import ListAppointmentViewSet
from app_bookings.views import ListMedicalNoteViewSet

# Crear un router
router = DefaultRouter()
router.register(r'patients', PatientViewSet, basename='patients') # basename en minúsculas
router.register(r'doctors', DoctorViewSet, basename='doctors')  
router.register(r'department', ListDepartmentViewSet, basename='department')  
router.register(r'doctoravailability', ListDoctorAvailabilityViewSet, basename='doctoravailability')  
router.register(r'medicalnotes', ListMedicalNoteViewSet, basename='medicalnotes')  
router.register(r'appointments', ListAppointmentViewSet, basename='appointments')  

urlpatterns = [
    path('', include(router.urls) ),  # Incluir las rutas generadas por el router
]
