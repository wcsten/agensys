from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer

from django.shortcuts import get_object_or_404
from schedule.models import Patient, Procedure, Schedule
from restless.preparers import SubPreparer


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


class ProcedureResource(DjangoResource):
    preparer = FieldsPreparer(fields={
        'name': 'name',
        'description': 'description',
    })

    def list(self):
        return Procedure.objects.all()

    def create(self):
        return Procedure.objects.create(
            name=self.data['name'],
            description=self.data['description'],
        )

    def detail(self, pk):
        return get_object_or_404(Procedure, pk=pk)

    def update(self, pk):
        procedure = self.detail(pk)

        procedure.name = self.data['name']
        procedure.description = self.data['description']
        procedure.save()

        return procedure

    def delete(self, pk):
        procedure = self.detail(pk)
        procedure.delete()

        return "Procedimento Deletado"

    def is_authenticated(self):
        return True


class ScheduleResource(DjangoResource):
    patient_preparer = FieldsPreparer(fields={
        'id': 'pk',
        'name': 'name',
        'email': 'email',
    })

    procedure_preparer = FieldsPreparer(fields={
        'id': 'pk',
        'name': 'name',
        'description': 'description',
    })

    preparer = FieldsPreparer(fields={
        'patient': SubPreparer('patient', patient_preparer),
        'procedure': SubPreparer('procedure', procedure_preparer),
        'detail': 'detail',
        'date': 'date',
        'start_time': 'start_time',
        'end_time': 'end_time',
    })

    def list(self):
        return Schedule.objects.all()

    def create(self):
        return Schedule.objects.create(
            patient=self.data['patient'],
            procedure=self.data['procedure'],
            detail=self.data['detail'],
            date=self.data['date'],
            start_time=self.data['start_time'],
            end_time=self.data['end_time'],
        )

    def detail(self, pk):
        return get_object_or_404(Schedule, pk=pk)

    def update(self, pk):
        schedule = self.detail(pk)

        schedule.patient = self.data['patient']
        schedule.procedure = self.data['procedure']
        schedule.detail = self.data['detail']
        schedule.date = self.data['date']
        schedule.start_time = self.data['start_time']
        schedule.end_time = self.data['end_time']

        schedule.save()

        return schedule

    def delete(self, pk):
        schedule = self.detail(pk)
        schedule.delete()

        return "Agendamento Deletado"

    def is_authenticated(self):
        return True
