from .serializers import PatientSerializer
from .models import Patient

from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer

from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView

# GET /patients => Listar
# POST /patients => Crear
# GET /patients/<pk>/ => Detalle
# PUT /patients/<pk>/ => Actualizar
# DELETE /patients/<pk>/ => Borrar


# @api_view(['GET', 'POST']) # BASADA EN FUNCIONES
# def list_patients(request):
#     if request.method == 'GET':
#         patients = Patient.objects.all()
#         serializer = PatientSerializer(patients, many=True)
#         return Response(serializer.data)

#     if request.method == 'POST':
#         serializer = PatientSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True) # Necesitamos Validar
#         serializer.save()
#         return Response(status=status.HTTP_201_CREATED)


class ListPatientsView(APIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get(self, request):
        patients = Patient.objects.all()  # Retrieve all patients
        serializer = PatientSerializer(patients, many=True)  # Serialize the data
        return Response(serializer.data)

    def post(self, request):
        serializer = PatientSerializer(data=request.data)  # Deserialize the request data
        if serializer.is_valid():
            serializer.save()  # Save the new patient
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Respond with the created data
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# from rest_framework import viewsets
# class ListPatientsView(viewsets.ModelViewSet):
#     """
#     Vista para gestionar pacientes (CRUD).
#     """
#     # Si necesitas permisos o autenticación, puedes agregar `permission_classes` y `authentication_classes`
#     permission_classes = []  # O puedes usar IsAuthenticated
#     # allowed_methods = ['GET', 'POST']
#     queryset = Patient.objects.all()  # Recupera todos los pacientes
#     serializer_class = PatientSerializer  # Serializador a utilizar



@api_view(['GET', 'PUT', 'DELETE'])  # BASADA EN FUNCIONES
def detail_patient(request, pk):
    try:
        patient = Patient.objects.get(id=pk)
    except Patient.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PatientSerializer(patient)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = PatientSerializer(patient, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    if request.method == 'DELETE':
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
