from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import *
from django.views.generic import View , UpdateView 
from django.urls import reverse_lazy
from .models import Proveedores, Producto, Pedido, PedidoDetalle, EstadosPedidos, Deposito
from .forms import ProveedorCreateForms, ProductoCreateForms, ProductoProveedorCreateForm

#--------------
from django.shortcuts import render
from django.http import HttpResponse

'''
from weasyprint import HTML
from weasyprint.text.fonts import FontConfiguration
'''

# Create your views here.


def proveedores(request):
    #muestro los proveedores por defecto al admin
    
    if request.method == 'GET':
        HAS_ACCESS=False
        context={}
        if request.user.is_authenticated:
            if request.user.is_superuser:
                HAS_ACCESS = True
                lista_proveedores = Proveedores.objects.all().order_by('-estado_proveedor')                
                context['proveedores'] = lista_proveedores
                   
            context['HAS_ACCESS'] = HAS_ACCESS
                
            return render(request, 'proveedoresApp/proveedores.html', context)

#filtro por estado 
def proveedoresPorEstado(request,estado):
    #muestro los proveedores por defecto al admin
    HAS_ACCESS=False
    context={}
    if request.method == 'GET':
        if request.user.is_authenticated:
            if request.user.is_superuser:
                HAS_ACCESS = True
                if estado==1:#Activos
                    lista_proveedores = Proveedores.objects.filter(estado_proveedor=True)
                    context['proveedores'] = lista_proveedores
                    context['HAS_ACCESS'] = HAS_ACCESS
                    return render(request, 'proveedoresApp/proveedores.html', context)

                elif estado==2:#inactivos
                    lista_proveedores = Proveedores.objects.filter(
                        estado_proveedor=False)
                    context['proveedores'] = lista_proveedores
                    context['HAS_ACCESS'] = HAS_ACCESS
                    return render(request, 'proveedoresApp/proveedores.html', context)

                else:
                    return redirect('proveedores')



#Ficha completa proveedor
class ProveedorFichaView(View):
    def get(self,request,pk,*args,**kwargs):
        proveedor = get_object_or_404(Proveedores,pk=pk)

    
        #prov=Proveedores.objects.get(usuario=usuario) #busco a que prov pertenece
        lista_pedidos= Pedido.objects.filter(id_proveedor = pk)# busco sus pedidos

        context={
            'proveedor':proveedor,
            'pedidos':lista_pedidos
        }
        return render(request, 'proveedoresApp/proveedor_ficha.html', context)



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
class ProveedorUpdateView(UpdateView):
    model= Proveedores
    fields = ['nombre_proveedor', 'cif_proveedor',
              'domicilio_proveedor', 'tel_proveedor', 'mail_proveedor', 'logo_proveedor']
    template_name = 'proveedoresApp/edito_proveedores.html'
    
    def get_success_url(self):
        pk= self.kwargs['pk']
        return reverse_lazy('proveedor_ficha', kwargs={'pk': pk})



# ------------------------- VISTAS PRODUCTOS PROVEEDORES ----------------------------  

#Lista productos por proveedor
class ProductoListView(View):
    model= Producto
    template= 'productos/productos.html'
    
    def get(self,request, pk=None,*args,**kwargs):
        if request.user.is_authenticated:
            HAS_ACCESS = False
            if pk == None :           
                if self.request.user.is_superuser:
                    productos = Producto.objects.all().order_by('id_proveedor')
                   
                    HAS_ACCESS=True
                else:
                    usuario=self.request.user
                    proveedor= Proveedores.objects.filter(usuario=usuario).first()
                    productos = Producto.objects.filter(id_proveedor=proveedor.id).order_by('disponible_producto')
                    HAS_ACCESS = True
            else:
                productos = Producto.objects.filter(
                    id_proveedor=pk).order_by('disponible_producto')

                for prov in productos:
                    if self.request.user == prov.id_proveedor.usuario or self.request.user.is_superuser:
                        HAS_ACCESS = True
                    
      
        context={
            'productos':productos,
            'idProveedor':pk,
            'HAS_ACCESS':HAS_ACCESS
        }
        return render(request,self.template,context)
       


# MODIFICACION DE DATOS PRODUCTO
class ProductoUpdateView(UpdateView):
    model = Producto
    fields = ['nombre_producto', 'descripcion_producto',
              'precio_producto', 'disponible_producto', 'imagen_producto']
    template_name = 'productos/edito_producto.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        proveedor=Producto.objects.get(pk=pk)
        proveedor = proveedor.id_proveedor.id
        return reverse_lazy('productos_proveedor', kwargs={'pk': proveedor})



#Creación de nuevo producto

class ProductoCreateView(View):
    def get(self,request,pk=None,*args,**kwargs):
        if self.request.user.is_authenticated:
            
            if pk==None:
                if self.request.user.is_superuser:
                    

                    form = ProductoCreateForms()
                else:
                    usuario= self.request.user
                    proveedor= Proveedores.objects.filter(usuario=usuario).first()
                    pk=proveedor.id
                    form = ProductoProveedorCreateForm()
           
            else:

                form = ProductoProveedorCreateForm()

            context = {
                'form': form,
                'idProveedor': pk
            }
       
        return render(request,'productos/nuevo_producto.html',context)
    
    def post(self,request,*args,**kwargs):
        if request.method=='POST':

            id_proveedor=int(request.POST['id_proveedor'])
            forms = ProductoCreateForms(request.POST, request.FILES)
            
            if forms.is_valid():
                
                id_proveedor = forms.cleaned_data.get('id_proveedor')
                nombre_producto=forms.cleaned_data.get('nombre_producto')
                imagen_producto = request.FILES.get('imagen_producto')
                descripcion_producto = forms.cleaned_data.get(
                    'descripcion_producto')
                precio_producto = forms.cleaned_data.get('precio_producto')
                disponible_producto = forms.cleaned_data.get(
                    'disponible_producto')

                create = Producto.objects.create(
                    id_proveedor=id_proveedor, nombre_producto=nombre_producto, imagen_producto=imagen_producto, descripcion_producto=descripcion_producto, precio_producto=precio_producto, disponible_producto=disponible_producto)
                
                create.save()

        return redirect('productos_proveedor',id_proveedor.id)


# ------------------------- VISTAS PEDIDOS  ----------------------------



#Armado de pedido

class PedidoCreateView(View):
    
    def post(self,request,*args,**kwargs):
        if request.method == 'POST':
            
            listaProductos = request.POST.getlist("idproductopedido")
            productos=[]
            
            #Busco los objetos productos
            for d in listaProductos:
                productos.append(Producto.objects.get(id=int(d),disponible_producto=True))
 
            context={
                'productos': productos,
                
            }
        
        return render(request,'pedidos/nuevo_pedido.html',context)


#Confirmo Pedido y guardo en su tabla

class ConfirmoPedidoProveedor(View):
    def post(self, request, *args, **kwargs):
        if request.method=="POST":
            if self.request.user.is_authenticated:
                #validar que tenga permiso

                listaProductos = request.POST.getlist("productoSolicitado")
                cantidadPedida= request.POST.getlist("cantSolicitada")               
                productos=[]
                
                #Busco los objetos productos
                for d in listaProductos:
                    productos.append(Producto.objects.get(id=int(d),disponible_producto=True))

                    ordenes_por_proveedor={}
 
                #Armo Pedido
                
                estadoPendiente = EstadosPedidos.objects.filter(
                    nombre_estado='PENDIENTE')

                # busco deposito predefinido

                deposito = Deposito.objects.filter(es_predefinido=True).first()

                pedido = Pedido(
                    id_proveedor=productos[0].id_proveedor, estado_pedido=estadoPendiente[0], id_deposito=deposito)
                pedido.save()

                #obtengo el id del pedido creado

                pedido= Pedido.objects.order_by('-id').first()
                
                
                #Armo Detalle Pedido
                
                for producto in productos:
                        
                    if int(cantidadPedida[productos.index(producto)]) >0: #no guardo productos sin cantidad
                        detalle = PedidoDetalle(numeroPedido=pedido, idproducto=producto, cant_pedida=cantidadPedida[productos.index(producto)])
                        detalle.save()
            
                return redirect('pedidos')



                

#Muestro lista de pedidos
class PedidosView(View):
    
    def get(self, request,*args,**kwargs):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                
                lista_pedidos = Pedido.objects.all().order_by('-updated')  # ve todos los pedidos
                
            else:   
                usuario= self.request.user.id #obtengo el user logueado
                prov=Proveedores.objects.get(usuario=usuario) #busco a que prov pertenece
                lista_pedidos = Pedido.objects.filter(
                    id_proveedor=prov).order_by('-updated')  # busco sus pedidos
                
            
            context={
                'pedidos':lista_pedidos
            }

        return render(request,'pedidos/pedidos.html',context)

#armo vista Detalle pedido
class DetallePedidoView(View):
    def get(self,request, pedido_id,*args,**kwargs):
        HAS_ACCESS = False
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:

                detalle_pedido = PedidoDetalle.objects.filter(numeroPedido=pedido_id)
                
                #traigo deposito
               
                deposito = Deposito.objects.get(
                    nombre_deposito=detalle_pedido[0].numeroPedido.id_deposito)
                
                #estados

                

                HAS_ACCESS=True
            else:
                usuario = self.request.user  # obtengo el user logueado
                # busco a que prov pertenece
                prov = Proveedores.objects.get(usuario=usuario)
                
                #obtengo los detalles
                detalle_pedido = PedidoDetalle.objects.filter(
                    numeroPedido=pedido_id)
                
                #traigo deposito
                deposito = Deposito.objects.get(nombre_deposito=detalle_pedido[0].numeroPedido.id_deposito)

                
                
                #valido que ese detalle/pedido pertenezca al proveedor/user logueado
                if prov == detalle_pedido[0].numeroPedido.id_proveedor:
                    HAS_ACCESS = True

            context = {
                'detalle_pedido': detalle_pedido,
                'HAS_ACCESS':HAS_ACCESS ,
                'deposito':deposito,
                
            }

            
            return render(request,'pedidos/detalle_pedido.html',context)

#Modifica estado del pedido

def cambiaEstadoPedido(request,pedido_id,id_estado):

    if request.user.is_authenticated:
        usuario = request.user
        pedido= Pedido.objects.get(id=pedido_id)
        
        if usuario.is_superuser or usuario == pedido.id_proveedor.usuario:
            
            estados=EstadosPedidos.objects.get(id=id_estado)
            if id_estado == 5:
                #Solo puede ponerlo como 'entregado' un superuser/admin, nunca el proveedor
                if usuario.is_superuser:
                    pedido.estado_pedido= estados
            else:
                pedido.estado_pedido = estados
            pedido.save()

        return redirect('detalle_pedido', pedido_id)




'''
def export_pdf(request):

    context = {}
    html = render_to_string("report/report-pdf.html", context)

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = "inline; report.pdf"

    font_config = FontConfiguration()
    HTML(string=html).write_pdf(response, font_config=font_config)

    return response
'''  
    
    
    
    


   




