from django.contrib import admin
from .models import Categoria, Producto


class CategoriaAdmin(admin.ModelAdmin):
    # Personalizar el administrador
    list_display = ('id', 'nombre')


class ProductoAdmin(admin.ModelAdmin):
    # Que campo no queremos que aparezca
    exclude = ('creado_en', )
    # Personalizar el administrador
    list_display = ('id', 'nombre', 'stock', 'creado_en')

# Register your models here.
# Metodo para registrar los modelos de Categoria y Producto
# Donde CategoriaAdmin es el nombre de la clase y se le pasa a admin
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
