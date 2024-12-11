from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MedicationSKU
from .serializers import MedicationSKUSerializer
from django.db import IntegrityError, transaction
from rest_framework.permissions import IsAuthenticated
import json


# View for CRUD
class MedicationSKUViewSet(viewsets.ModelViewSet):
    queryset = MedicationSKU.objects.all()
    serializer_class = MedicationSKUSerializer

    @action(detail=False, methods=['post'], url_path='bulk_upload')
    def bulk_upload(self, request):
        try:
            data = request.data.get('skus', [])
            serializer = self.get_serializer(data=data, many=True)
            serializer.is_valid(raise_exception=True)
            with transaction.atomic():
                self.perform_bulk_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except IntegrityError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def perform_bulk_create(self, serializer):
        serializer.save()


# View for login
class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {'message': 'This is protected view'}
        return Response(content)