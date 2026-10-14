from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import Producto

class ProductoListView(ListView):
    model = Producto
    template_name = 'ventas/listar.html'
    paginate_by = 5

class ProductoCreateView(SuccessMessageMixin, CreateView):
    model = Producto
    fields = ['nombre', 'precio', 'stock']
    template_name = 'ventas/form.html'
    success_url = reverse_lazy('ventas:listar_productos')
    success_message = "¡Producto creado con éxito!"

class ProductoUpdateView(SuccessMessageMixin, UpdateView):
    model = Producto
    fields = ['nombre', 'precio', 'stock']
    template_name = 'ventas/form.html'
    success_url = reverse_lazy('ventas:listar_productos')
    success_message = "¡Producto actualizado correctamente!"

class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'ventas/eliminar.html'
    success_url = reverse_lazy('ventas:listar_productos')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "¡Producto eliminado con éxito!")
        return super().delete(request, *args, **kwargs)