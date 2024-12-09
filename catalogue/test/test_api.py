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
def test_bulk_upload(api_client):
    url = reverse('sku-bulk-upload')
    data = {
        "skus": [
            {
                "inn": "Ceftriaxone",
                "formulation": "Injectable Solution",
                "dosage": "64",
                "unit": "G"
            },
            {
                "inn": "Ibuprofen",
                "formulation": "Tablet",
                "dosage": "200",
                "unit": "mg"
            }
        ]
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == 201
    assert MedicationSKU.objects.count() == 2
