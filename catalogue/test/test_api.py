# catalogue/tests/test_api.py

import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from catalogue.models import MedicationSKU

@pytest.fixture
def api_client():
    return APIClient()

@pytest.mark.django_db
def test_create_sku(api_client):
    url = reverse('sku-list')
    data = {
        "inn": "Amoxicillin",
        "formulation": "Tablet",
        "dosage": "50",
        "unit": "mg"
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == 201
    assert MedicationSKU.objects.count() == 1
    assert MedicationSKU.objects.get().inn == "Amoxicillin"

@pytest.mark.django_db
def test_create_duplicate_sku(api_client):
    url = reverse('sku-list')
    data = {
        "inn": "Amoxicillin",
        "formulation": "Tablet",
        "dosage": "50",
        "unit": "mg"
    }
    # Crear el primer SKU
    response1 = api_client.post(url, data, format='json')
    assert response1.status_code == 201
    assert MedicationSKU.objects.count() == 1

    # Intentar crear un SKU duplicado
    response2 = api_client.post(url, data, format='json')
    assert response2.status_code == 400  # O el código de error que hayas definido
    assert "unique" in response2.data['non_field_errors'][0].lower()
    assert MedicationSKU.objects.count() == 1  # Asegurar que no se añadió el duplicado
