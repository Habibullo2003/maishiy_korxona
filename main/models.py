from django.db import models
from django.utils import timezone


class Korxona(models.Model):
    nomi = models.CharField(max_length=200)
    manzil = models.CharField(max_length=255)
    telefon = models.CharField(max_length=20)
    faoliyat_turi = models.CharField(max_length=100)
    ochilgan_sana = models.DateField()
    ishchi_soni = models.IntegerField()
    qayta_ishlaydigan_materiallar = models.TextField()
    izoh = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nomi
