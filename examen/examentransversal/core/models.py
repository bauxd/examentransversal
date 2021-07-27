from django.db import models
from django.db.models.fields import IntegerField


# Create your models here.
class producto(models.Model):
    producto=models.CharField(max_length=50,primary_key=True,null=True)

class infocompra(models.Model):
    nombre=models.CharField(max_length=30,primary_key=True)
    apellido=models.CharField(max_length=30)
    rut=models.CharField(max_length=15)
    direccion=models.CharField(max_length=30)
    correo=models.CharField(max_length=40)
    producto=models.ForeignKey(producto, on_delete=models.CASCADE)

    def _str_(self):
        return self.nombre



