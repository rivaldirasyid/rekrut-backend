from django.db import models

class Kriteria(models.Model):
    nama = models.CharField(max_length=100)
    bobot = models.FloatField()  # Bobot kriteria (0-1)

    def __str__(self):
        return f"{self.nama} ({self.bobot})"

class Kandidat(models.Model):
    nama = models.CharField(max_length=255)
    pendidikan = models.IntegerField()  # Skor pendidikan (1-5)
    pengalaman = models.IntegerField()  # Skor pengalaman (1-10)
    kemampuan_teknis = models.FloatField()  # Skor teknis (0-100)
    soft_skills = models.FloatField()  # Skor soft skills (1-5)

    def __str__(self):
        return self.nama
