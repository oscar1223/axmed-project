# catalogue/serializers.py

from rest_framework import serializers
from .models import MedicationSKU
from fuzzywuzzy import fuzz

class MedicationSKUSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicationSKU
        fields = '__all__'

    def validate_inn(self, value):
        existing_inns = MedicationSKU.objects.values_list('inn', flat=True)
        for existing_inn in existing_inns:
            similarity = fuzz.ratio(existing_inn.lower(), value.lower())
            if similarity > 90:  # Umbral de similitud
                raise serializers.ValidationError(
                    f"El nombre INN '{value}' es similar a '{existing_inn}'."
                )
        return value

    def validate(self, data):
        # Validar unicidad de la combinación de campos
        if MedicationSKU.objects.filter(
            inn=data['inn'],
            formulation=data['formulation'],
            dosage=data['dosage'],
            unit=data['unit']
        ).exists():
            raise serializers.ValidationError("Esta combinación de campos ya existe.")
        return data
