from django.shortcuts import redirect, render
from django.contrib.auth import *
from django.views.generic import View
from .models import Proveedores
from .forms import ProveedorCreateForms

# Create your views here.


def proveedores(request):
    #muestro los proveedores por defecto al admin
   
    if request.method == 'GET':
        lista_proveedores = Proveedores.objects.all()
        context = {'proveedores': lista_proveedores}
        return render(request, 'proveedoresApp/proveedores.html', context)


def proveedoresPorEstado(request,estado):
    #muestro los proveedores por defecto al admin

    if request.method == 'GET':
        if estado==1:
            lista_proveedores = Proveedores.objects.filter(estado_proveedor=True)
            context = {'proveedores': lista_proveedores}
            return render(request, 'proveedoresApp/proveedores.html', context)
        elif estado==2:
            lista_proveedores = Proveedores.objects.filter(
                estado_proveedor=False)
            context = {'proveedores': lista_proveedores}
            return render(request, 'proveedoresApp/proveedores.html', context)
        else:
            return redirect('proveedores')



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


#Formulario creación Proveedor
class ProveedorCreateView(View):
    def get(self,request,*args,**kwargs):
        forms=ProveedorCreateForms()
        context={'form':forms}
        return render(request, 'proveedoresApp/nuevo_proveedor.html',context)

    def post(self, request, *args, **kwargs):
        
        if request.method=='POST':
            
            forms = ProveedorCreateForms(request.POST, request.FILES)
            
            if forms.is_valid():
                
                nombre_proveedor = forms.cleaned_data.get('nombre_proveedor')
                cif_proveedor = forms.cleaned_data.get('cif_proveedor')
                domicilio_proveedor = forms.cleaned_data.get(
                    'domicilio_proveedor')
                tel_proveedor = forms.cleaned_data.get('tel_proveedor')
                mail_proveedor = forms.cleaned_data.get('mail_proveedor')
                logo_proveedor = request.FILES.get('logo_proveedor')
                
                create = Proveedores.objects.create(
                    nombre_proveedor=nombre_proveedor, cif_proveedor=cif_proveedor, domicilio_proveedor=domicilio_proveedor, tel_proveedor=tel_proveedor,
                    mail_proveedor=mail_proveedor, logo_proveedor=logo_proveedor)
                create.save()
                     
        return redirect('proveedores')

# MODIFICACION DE DATOS PROVEEDOR
#ver como pasar parametros en classview
class EditProveedorView(View):
    def get(self,request,*args,**kwargs):
        
        if request.method == 'GET':
            proveedor = Proveedores.objects.get(id)
            proveedor.save()
            context = {
                'proveedor': proveedor
            }

            return render(request,'nuevo_proveedor', context)
