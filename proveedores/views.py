from django.shortcuts import redirect, render
from django.contrib.auth import *
from .models import Proveedores

# Create your views here.


def proveedores(request):
    #muestro los proveedores por defecto al admin
   
    if request.method == 'GET':
        lista_proveedores = Proveedores.objects.all()
        context = {'proveedores': lista_proveedores}
        return render(request, 'proveedoresApp/proveedores.html', context)


#Ficha completa proveedor
def proveedor_ficha(request,id_proveedor):

    if request.method == 'GET':
        proveedor= Proveedores.objects.get(id=id_proveedor)
        context = {
            'proveedor' : proveedor
        }

        return render(request, 'proveedoresApp/proveedor_ficha.html',context)

#Pongo inactivo al proveedor


def inactivo_proveedor(request, id_proveedor):
    
    if request.method == 'GET':
        proveedor = Proveedores.objects.get(id=id_proveedor)
        
        proveedor.estado_proveedor = not (proveedor.estado_proveedor)
        

        proveedor.save()
        
        
        context = {
            'proveedor': proveedor
        }

        return redirect('proveedor_ficha',id_proveedor)


