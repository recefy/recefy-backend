from django.db import models


class Usuarios(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    url_image = models.CharField(max_length=255)