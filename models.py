"""Models of QR app"""
from django.db import models
from apps.admin2.models import Local

class QRCode(models.Model):
    img = models.URLField(
            verbose_name = 'Imagen',
            )
    #este es un contador de cuantas veces se usa este codigoQR
    counter = models.IntegerField(
            default = 0
            )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

