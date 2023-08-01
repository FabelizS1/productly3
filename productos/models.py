from django.db import models
from django.utils import timezone

# Create your models here.
# Debe heredar de los modelos de Django
class Categoria(models.Model):
    # CharField: Es una cadena de texto pero limitada, max_length es la longitud maxima
    # no se agrega el id porque el lo crea de forma automatica
    nombre = models.CharField(max_length=255)

    # Con esto se transforma la categoria en un string
    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    # numero de productosa en stock
    stock = models.IntegerField()
    # Dar una puntuacion
    puntaje = models.FloatField()
    # Es la categoria y para relacionarla con la otra tabla se hace con ForeignKey
    # Tipos de on_delete:
    # CASCADE: Elimina el producto si se elimina la categoria
    # PROTECT: Lanza un error no deja eliminar la categoria
    # RESTRICT: No deja eliminar la categoria a menos que haya eliminado todos los productos
    # SET_NULL: Setea un valor nulo si se elimina la categoria
    # SET_DEFAULT: Asigna valor por defecto, si se usa default es asi categoria = models.ForeignKey(Categoria, default=1, on_delete=)
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.CASCADE
    )


    # Cuando fue creado este producto
    # Esto es para hacer de forma automatica
    # Va a ser la referencia todos los archivos se 
    # van a crear en esa fecha
    # Se agrega a todas las tablas
    creado_en = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre