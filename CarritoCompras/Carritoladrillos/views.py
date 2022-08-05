from django.shortcuts import redirect, render,HttpResponse
from Carritoladrillos.Carrito import Carrito
from Carritoladrillos.models import Propiedad

# Create your views here.
def tienda (request):
    
    propiedades= Propiedad.objects.all()
    return render(request, "tienda.html", {'propiedades':propiedades})

def agregar_propiedad(request, propiedad_id):
    carrito=Carrito(request)
    propiedad = Propiedad.objects.get(id=propiedad_id)
    #hereda de Carrito.py
    carrito.agregar(propiedad)                           
    return redirect("Tienda")

def eliminar_propiedad (request,propiedad_id):
    carrito=Carrito(request)
    propiedad = Propiedad.objects.get(id=propiedad_id)
    carrito.eliminar(propiedad)
    return redirect("Tienda")

def restar_propiedad (request,propiedad_id):
    carrito=Carrito(request)
    propiedad = Propiedad.objects.get(id=propiedad_id)
    carrito.restar(propiedad)
    return redirect("Tienda")

def limpiar (request):
    carrito=Carrito(request)
    carrito.limpiar()
    return redirect("Tienda")