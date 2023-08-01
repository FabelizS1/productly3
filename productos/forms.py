# El modelo por ejemplo productos va al ModelForm y este va 
# crear la vista 
from . import models
from django.forms import ModelForm


class ProductoForm(ModelForm):
    # Cuando se usa ModelForm se debe crear otra clase que en este caso es Meta
    class Meta:
        # Aqui indicamos el modelo para crear el formulario
        model = models.Producto
        # Aqui indicamos los formularios que queremos que tenga, va a contener una lista con los nombres
        # exactos que queremos que aparezcan en el formulario
        fields = ['nombre', 'stock', 'puntaje', 'categoria']
