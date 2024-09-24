from django.test import TestCase

# Create your tests here.


from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from app_patients.models import Patient
from .models import Doctor


# Vamos a validar que el Listado de Appointments funcione correctamente.
class DoctorViewSetTests(TestCase):

    def setUp(self):
        # Paciente de Ejemplo
        self.patient = Patient.objects.create(
            first_name='Luis',
            last_name='Martinez',
            date_of_birth='1990-12-05',
            contact_number='12312312',
            email='example@example.com',
            address='Dirección de prueba',
            medical_history='Ninguna',
        )
        #Doctor de Ejemplo
        self.doctor = Doctor.objects.create(
            first_name='Oscar',
            last_name='Barajas',
            qualification='Profesional',
            contact_number='23412341234',
            email='example2@example.com',
            address='Medellín',
            biography='Sin',
            is_on_vacation=False,
        )
        # API Client: Nos va a permitir simular requests a nuestro código
        self.client = APIClient()

    def test_list_should_return_200(self):
        url = reverse( # NO SE PUEDE ACCEDER A LA PAGINA SIN AUTENTICACION Y AUTORIZACION, RECIBIREMOS UN 403
            'doctors-appointments',
            kwargs={"pk": self.doctor.id},
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)