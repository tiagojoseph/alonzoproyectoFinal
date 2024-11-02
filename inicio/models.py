from django.db import models

class Casa (models.Model):
    ubicacion = models.CharField(max_length=20)
    ambientes = models.IntegerField()
    precio = models.CharField (max_length=20)

    def __str__(self):
        return f"{self.ubicacion} {self.precio} "
