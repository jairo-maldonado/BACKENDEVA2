from django.views.generic import ListView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from .models import Producto

class ProductoListView(ListView):
    model = Producto
    template_name = 'producto_list.html'
    paginate_by = 5

class ProductoCreateView(SuccessMessageMixin, CreateView):
    model = Producto
    fields = ['nombre', 'precio', 'stock']
    template_name = 'producto_form.html'
    success_url = '/'
    success_message = "¡El producto %(nombre)s fue creado exitosamente!"