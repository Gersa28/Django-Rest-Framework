from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import DoctorSerializer
from .serializers import DepartmentSerializer
from .serializers import DoctorAvailabilitySerializer
from .serializers import DoctorAvailabilitySerializer
from .models import Doctor
from .models import Department
from .models import DoctorAvailability
from .models import MedicalNote
from .permissions import IsDoctor
from app_bookings.serializers import AppointmentSerializer
from app_bookings.models import Appointment



class DoctorViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
    permission_classes = [IsAuthenticated, IsDoctor] # Solo podrá editar quien sea autenticado y, además, doctor.

    @action(['POST'], detail=True, url_path='set-on-vacation') # detail = True, modifica solo un item, usa la pk o id
    def set_on_vacation(self, requests, pk):
        doctor = self.get_object() # Trae al doctor con el pk = id
        doctor.is_on_vacation = True
        doctor.save()
        return Response({"status": "El doctor está en vacaciones"})

    @action(['POST'], detail=True, url_path='set-off-vacation')
    def set_off_vacation(self, requests, pk):
        doctor = self.get_object()
        doctor.is_on_vacation = False
        doctor.save()
        return Response({"status": "El doctor NO está en vacaciones"})
    
    @action(['POST', 'GET'], detail=True, serializer_class=AppointmentSerializer)
    def appointments(self, request, pk):
        doctor = self.get_object()

        if request.method == 'POST':
            # serializer = AppointmentSerializer(request.data) # Si HIcieramos esto el Doctor podría elegir otro Doctor
            data = request.data.copy() # Tomamos lo que ingresa el Usuario.
            data['doctor'] = doctor.id # SOLO PUEDE AGENDAR CITAS SERA PARA SI MISMO, FIJAMOS EL ID.
            serializer = AppointmentSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        if request.method == 'GET':
            appointments = Appointment.objects.filter(doctor=doctor)
            serializer = AppointmentSerializer(appointments, many=True)
            return Response(serializer.data)
        
class ListDepartmentViewSet(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
    
class ListDoctorAvailabilityViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorAvailabilitySerializer
    queryset = DoctorAvailability.objects.all()

class ListMedicalNoteViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorAvailabilitySerializer
    queryset = MedicalNote.objects.all()