from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer

from django.shortcuts import get_object_or_404
from schedule.models import Patient, Procedure, Schedule


class PatientResource(DjangoResource):
    preparer = FieldsPreparer(fields={
        'name': 'name',
        'email': 'email',
    })

    def list(self):
        return Patient.objects.all()

    def create(self):
        return Patient.objects.create(
            name=self.data['name'],
            email=self.data['email'],
        )

    def detail(self, pk):
        return get_object_or_404(Patient, pk=pk)

    def update(self, pk):
        patient = self.detail(pk)

        patient.name = self.data['name']
        patient.email = self.email['email']
        patient.save()

        return patient

    def delete(self, pk):
        patient = self.detail(pk)
        patient.delete()

        return "Paciente Deletado"

    def is_authenticated(self):
        return True
