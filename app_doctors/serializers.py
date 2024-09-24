from rest_framework import serializers

from .models import Doctor, Department, DoctorAvailability, MedicalNote


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

    def validate_email(self, value):
        if "@example.com" in value: # Solo se admiten emails corporativos
            return value
        raise serializers.ValidationError("El correo debe incluir @example.com") # Excepción Customizada

    def validate(self, attrs): # Validaremos el número de contacto con el diccionario attrs
        # attrs['email']  acá tenemos un diccionario con el formulario
        if len(attrs['contact_number']) < 10:
            raise serializers.ValidationError(
                "Por favor, ingrese un número válido "
            )
        return super().validate(attrs)


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class DoctorAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorAvailability
        fields = '__all__'


class MedicalNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalNote
        fields = '__all__'