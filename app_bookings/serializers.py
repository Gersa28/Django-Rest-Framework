from rest_framework import serializers
from .models import Appointment, MedicalNote


from rest_framework import serializers
from .models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    doctor_name = serializers.SerializerMethodField()  # Campo para mostrar el nombre del doctor

    class Meta:
        model = Appointment
        fields = '__all__'

    # Método para obtener el nombre completo del doctor
    def get_doctor_name(self, obj):
        # Verificamos si existe un doctor asociado a la cita
        if obj.doctor:
            return f"{obj.doctor.first_name} {obj.doctor.last_name}"
        return None  # Si no hay doctor, devolvemos None o un valor alternati

class MedicalNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalNote
        fields = '__all__'