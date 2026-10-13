from django.contrib import admin
from .models import Producto, Cliente, Venta

admin.site.site_header = "Administración de Inventario BackendU2"
admin.site.site_title = "Panel BackendU2"
admin.site.index_title = "Panel de Control de Jairo"

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock')
    search_fields = ('nombre',)
    list_filter = ('stock',)