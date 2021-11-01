from django.shortcuts import render
from .models import Proveedores

# Create your views here.


def proveedores(request):

    lista_proveedores = Proveedores.objects.all()

    data = {'proveedores': lista_proveedores}
    return render(request, 'proveedoresApp/proveedores.html', data)
