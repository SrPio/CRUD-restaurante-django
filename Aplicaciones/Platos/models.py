from django.db import models

# Create your models here.
class Plato(models.Model):
    codigo=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    tiempo=models.CharField(max_length=360)
    categoria=models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Alimento(models.Model):
    nombre=models.CharField(max_length=50)
    categoria=models.CharField(max_length=20)
    plato = models.ForeignKey(Plato, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre