from django.shortcuts import render, redirect
from .models import Plato
from .models import Alimento
from django.contrib import messages

# Create your views here.
def home(request):
    platosListados = Plato.objects.all()
    alimentosListados = Alimento.objects.all()
    return render(request, "gestionPlatos.html", {"platos": platosListados, "alimentos": alimentosListados})

def registarPlato(request):
    codigo=request.POST.get("txtCodigo")
    nombre=request.POST.get("txtNombre")
    categoria=request.POST.get("txtCategoria")
    tiempo=request.POST.get("tiempo")

    plato = Plato.objects.create(codigo=codigo, nombre=nombre, categoria=categoria, tiempo=tiempo)
    messages.success (request, '¡Plato Registrado!')
    return redirect('/')

def registarAlimento(request):
    nombre=request.POST.get("txtNombreAlimento")
    categoria=request.POST.get("txtCategoriaAlimento")
    plato_id=request.POST.get("plato")
    plato=Plato.objects.get(codigo=plato_id)

    alimento = Alimento.objects.create(nombre=nombre, categoria=categoria, plato=plato)
    messages.success (request, '¡Alimento Registrado!')
    return redirect('/')

def edicionPlato(request, codigo):
    plato = Plato.objects.get(codigo=codigo)
    return render(request, 'edicionPlato.html', {"plato": plato})

def editarPlato(request):
    codigo=request.POST.get("txtCodigo")
    nombre=request.POST.get("txtNombre")
    categoria=request.POST.get("txtCategoria")
    tiempo=request.POST.get("tiempo")

    plato = Plato.objects.get(codigo=codigo)
    plato.nombre = nombre
    plato.categoria = categoria
    plato.tiempo = tiempo
    plato.save()

    messages.success (request, '¡Plato Modificado!')
    return redirect('/')

def eliminacionPlato(request, codigo):
    plato = Plato.objects.get(codigo=codigo)
    plato.delete()

    messages.success (request, '¡Plato Eliminado!')
    return redirect('/')

"""---------------------"""

def edicionAlimento(request, id):
    alimento = Alimento.objects.get(id=id)
    return render(request, 'edicionAlimento.html', {"alimento": alimento})

def editarAlimento(request):
    id=request.POST.get("id")
    nombre=request.POST.get("txtNombre")
    categoria=request.POST.get("txtCategoria")
    plato=request.POST.get("plato")

    alimento = Alimento.objects.get(id=id)
    alimento.nombre = nombre
    alimento.categoria = categoria
    alimento.save()

    messages.success (request, '¡Alimento Modificado!')
    return redirect('/')

def eliminacionAlimento(request, id):
    alimento = Alimento.objects.get(id=id)
    alimento.delete()

    messages.success (request, '¡Alimento Eliminado!')
    return redirect('/')