from django.db import models

# Create your models here.
class usuario(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100, null=True, blank=True)
    direccion_calle = models.CharField(max_length=100, null=True, blank=True)
    direccion_numero = models.CharField(max_length=30, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        retorno = "{0} - {1} - {2}".format(self.id, self.username, self.email)
        return retorno
