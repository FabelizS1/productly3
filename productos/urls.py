from django.urls import path
# importa el archivo de views.py de productos
from . import views
# Django valida que exista esta variable app_name, si existe va a concatenar el nombre con el 
# name de path
app_name = 'productos'

urlpatterns = [
    # solo /productos
    # donde views.index es el nombre de la funcion en el archivo de views y 
    # name es el nombre que va a tener
    path('', views.index, name='index'),
    path('formulario', views.formulario, name='formulario'),
    # Nombre del parametro que es producto_id
    # Referencia a una url se usa <a></a> href  productos/1
    path(
        # '<producto_id>' permite todo tipo de datos y si solo se quiere que sea de un tipo como
        #  solo entero <int:producto_id>
        '<int:producto_id>', 
        views.detalle, 
        # Se puede poner asi name='producto_detalle'
        name='detalle'
        )


]