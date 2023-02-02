from django.shortcuts import render
from rest_framework.response import Response
# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .serializer import *
from rest_framework.decorators import action
from students.models import *
import codecs
import csv
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from datetime import datetime
fs = FileSystemStorage(location='tmp/')

class StudentViewset(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context
class DavomatViewset(ModelViewSet):
    queryset = Davomat.objects.all()
    serializer_class = DavomatSerializer
    def create(self, request, *args, **kwargs):
        data = request.data
        if 'students' in data:

            for student in data['students']:
                try:
                    talaba = Student.objects.get(id=student['id'])
                    print(talaba.name)
                    Davomat.objects.create(student=talaba,status=student['status'],description=student.get('description','Sabab korsatilmagan'))
                except Student.DoesNotExist:
                    pass
            return Response("Davomat olindi!")
        else:
            return Response('Student Doesnt Found')
    def partial_update(self, request, *args, **kwargs):
        davomat_data = self.get_object()
        data = request.data
        if 'students' in data:
           for student in data['students']:
                try:
                    student = Student.objects.get(id=student['id'])
                    davomat_data.student =student
                    davomat_data.description = student.get('description',davomat_data.description)
                    davomat_data.status = student.get('status',davomat_data.status)
                    davomat_data.date = student.get('date',davomat_data.date)
                    serializer = DavomatSerializer(davomat_data)
                    return Response(serializer.data)
                except Student.DoesNotExist:
                    return Response('Student not found')
        else:
            return Response('student field required')
    def update(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
            
class TestViewset(ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    @action(detail=False, methods=['POST'])
    def upload_data(self, request):
        file = request.FILES["file"]
        content = file.read()
        file_content = ContentFile(content)
        file_name = fs.save(
            "_tmp.csv", file_content
        )
        tmp_file = fs.path(file_name)
        csv_file = open(tmp_file, errors="ignore")
        reader = csv.reader(csv_file)
        next(reader)
        results_list = []
        for id_, row in enumerate(reader):
            (
                test_kodi,
                fan_nomi,
                talaba,
                telefon_raqam,
                savollar_soni,
                togri_javoblar
            ) = row
            results_list.append(
                Test(
                    test_kodi=test_kodi,
                    fan_nomi=fan_nomi,
                    talaba=talaba,
                    telefon_raqam=telefon_raqam,
                    savollar_soni=savollar_soni,
                    togri_javoblar=togri_javoblar,
                )
            )
        print(results_list)
        Test.objects.bulk_create(results_list)
        return Response("Successfully upload the data")

    @action(detail=False, methods=['POST'])
    def upload_data_with_validation(self, request):
        file = request.FILES.get("file")
        reader = csv.DictReader(codecs.iterdecode(file, "utf-8"), delimiter=",")
        data = list(reader)
        serializer = self.serializer_class(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        results_list = []
        for row in serializer.data:
            results_list.append(
                Test(
                    test_kodi=row["test_kodi"],
                    fan_nomi=row["fan_nomi"],
                    talaba=row["talaba"],
                    telefon_raqam=row['telefon_raqam'],
                    savollar_soni=row["savollar_soni"],
                    togri_javoblar=row["togri_javoblar"],

                )
            )
        Test.objects.bulk_create(results_list)
        return Response("Successfully upload the data")
        
