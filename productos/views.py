#from django.http import HttpResponse, JsonResponse
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .forms import ProductoForm
# Hay que agregar el . al principio
from .models import Producto

# Create your views here.

# Todas las vistas se le agrega de parametro request
# /productos
# def index(request):
#    return HttpResponse('Hola Mundo!')



def index(request):
    # Para buscar todos los productos
    # productos = Producto.objects.all()
    # Se le agrega .values() para que muestre los valores
    # productos = Producto.objects.all().values()
    productos = Producto.objects.all()
    # Para filtrar por un producto,  o todos los puntajes mayores o igual puntaje__gte=3, o puede ser
    # menor o igual puntaje__lte=3, o menor puntaje__lt=3, o mayor que puntaje__gt=3 
    #productos = Producto.objects.filter(puntaje=5)
    # Para buscar un elemento en particular o pk=1 que seria el primary key
    #productos = Producto.objects.get(id=5)

    ## print(productos)
    # return HttpResponse('hola mundo')
    # return HttpResponse(productos[0].nombre)
    # Si no se coloca safe=False no trae la informacion
    ## return JsonResponse(list(productos), safe=False)
    return render(
        request, 
        # Donde se encuentra la plantilla y el nombre de la plantilla
        'index.html',
        # Los datos que se le pasan a la plantilla
        # Le pasamos la informacion de los productos
        context={'productos': productos}
    )


# producto_id es el nombre del parametro que se agrego en productos/urls.py
def detalle(request, producto_id):
    # Con la clase de Producto que es la que se necesita, luego se define el id que es por el 
    # que se va a buscar la informacion en la base de datos
    #try:
    #producto=
    #except Producto.DoesNotExists:
    #raise Http404()


    producto = get_object_or_404(Producto, id=producto_id)

    return render(
        request, 
        'detalle.html', 
        context={ 'producto':producto }
        )


def formulario(request):

    if request.method == 'POST':
        # crear un formulario en funcion a la clase que se creo que es ProductoForm() en el archivo de Form
        form = ProductoForm(request.POST)
        # Validar si el formulario es valido
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/productos')
    else:
        # Crear formulario
        form = ProductoForm()

            
    return render(
        request, 
        'producto_form.html',
        # este es un diccionario que contiene la informacion, donde form es el objeto de arriba
        # si ocurre un error de validacion igual se va por aqui y muestra los errores
        {'form': form}
    )

    ## Agregando get_object_or_404 en el import se puede agregar hacer esto de forma reducida
    ## sin el try except
    ## try:
    ##     #return HttpResponse(producto_id)
    ##     producto = Producto.objects.get(id=producto_id)
        
    ##     return render(
    ##         request, 
    ##         'detalle.html', 
    ##         context={ 'producto':producto }
    ##         )
    # Se coloca en el except Producto.DoesNotExist porque este error extiende de Producto
    ## except Producto.DoesNotExist:
    ##     raise Http404()









