from django.db import models

# Create your models here.
class MedicationSKU(models.Model):
    inn = models.CharField(max_length=255, unique=True)
    formulation = models.CharField(max_length=255)
    dosage = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=50)

    class Meta:
        unique_together = ('inn', 'formulation', 'dosage', 'unit')

    def __str__(self):
        return f"{self.inn} - {self.formulation} - {self.dosage}{self.unit}"