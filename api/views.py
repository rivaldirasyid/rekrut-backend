from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Max
from .models import Kandidat, Kriteria
from .serializers import KandidatSerializer, KriteriaSerializer

class KriteriaList(APIView):
    def get(self, request):
        kriteria = Kriteria.objects.all()
        serializer = KriteriaSerializer(kriteria, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = KriteriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class KandidatList(APIView):
    def get(self, request):
        kandidat = Kandidat.objects.all()
        serializer = KandidatSerializer(kandidat, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = KandidatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SAWCalculator(APIView):
    def get(self, request):
        kandidat = Kandidat.objects.all()
        kriteria = Kriteria.objects.all()

        if not kriteria.exists():
            return Response({"error": "Kriteria belum diatur."}, status=400)

        max_values = {
            "pendidikan": Kandidat.objects.aggregate(Max("pendidikan"))["pendidikan__max"],
            "pengalaman": Kandidat.objects.aggregate(Max("pengalaman"))["pengalaman__max"],
            "kemampuan_teknis": Kandidat.objects.aggregate(Max("kemampuan_teknis"))["kemampuan_teknis__max"],
            "soft_skills": Kandidat.objects.aggregate(Max("soft_skills"))["soft_skills__max"],
        }

        hasil = []
        for k in kandidat:
            skor = 0
            if max_values["pendidikan"]:
                skor += (k.pendidikan / max_values["pendidikan"]) * kriteria.get(nama="pendidikan").bobot
            if max_values["pengalaman"]:
                skor += (k.pengalaman / max_values["pengalaman"]) * kriteria.get(nama="pengalaman").bobot
            if max_values["kemampuan_teknis"]:
                skor += (k.kemampuan_teknis / max_values["kemampuan_teknis"]) * kriteria.get(nama="kemampuan_teknis").bobot
            if max_values["soft_skills"]:
                skor += (k.soft_skills / max_values["soft_skills"]) * kriteria.get(nama="soft_skills").bobot

            hasil.append({
                "nama": k.nama,
                "skor": skor,
                "pendidikan": k.pendidikan,
                "pengalaman": k.pengalaman,
                "kemampuan_teknis": k.kemampuan_teknis,
                "soft_skills": k.soft_skills,
            })

        hasil.sort(key=lambda x: x["skor"], reverse=True)
        return Response(hasil)
