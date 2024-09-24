from django.shortcuts import render
from rest_framework import viewsets

from .models import Appointment, MedicalNote
from .serializers import AppointmentSerializer, MedicalNoteSerializer


class ListAppointmentViewSet(viewsets.ModelViewSet):
    """
    Obtiene la lista de citas medicas programadas
    """
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()



class ListMedicalNoteViewSet(viewsets.ModelViewSet):
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()


