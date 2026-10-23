from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'principal/inicio.html')


def juegos(request):
    return render(request, 'principal/juegos.html')


def historia(request):
    return render(request, 'principal/historia.html')


def personajes(request):
    return render(request, 'principal/personajes.html')

def wiki(request):
    return render(request, 'principal/wiki.html')