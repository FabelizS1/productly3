from django.shortcuts import render

def inicio(request):
    return render(
        request,
        'inicio.html',
        # No se le pasa el tercer argumento porque no hay parametros es la pagina de inicio
    )