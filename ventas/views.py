from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Producto
from .forms import ProductoForm

def listar_productos(request):
    productos_lista = Producto.objects.all().order_by('id')
    paginator = Paginator(productos_lista, 5)
    page_number = request.GET.get('page')
    productos = paginator.get_page(page_number)
    return render(request, 'ventas/listar.html', {'productos': productos})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Producto creado exitosamente.")
            return redirect('listar_productos')
        else:
            messages.error(request, "Error al guardar. Revisa los datos.")
    else:
        form = ProductoForm()
    return render(request, 'ventas/form.html', {'form': form, 'titulo': 'Crear Producto'})

def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, "Producto actualizado exitosamente.")
            return redirect('listar_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'ventas/form.html', {'form': form, 'titulo': 'Editar Producto'})

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.delete()
        messages.success(request, "Producto eliminado.")
        return redirect('listar_productos')
    return render(request, 'ventas/eliminar.html', {'producto': producto})