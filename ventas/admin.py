from django.contrib import admin
from .models import Producto, Venta, DetalleVenta

# Branding personalizado del Panel de Administración
admin.site.site_header = "Administración de Inventario BackendU2"
admin.site.site_title = "Panel BackendU2"
admin.site.index_title = "Panel de Control de Jairo"


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock')
    search_fields = ('nombre',)
    list_filter = ('stock',)
    ordering = ('nombre',)


class DetalleVentaInline(admin.TabularInline):
    model = DetalleVenta
    extra = 1
    readonly_fields = ('subtotal',)


@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha', 'cliente', 'total')
    list_filter = ('fecha',)
    search_fields = ('cliente', 'id')
    readonly_fields = ('fecha', 'total')
    inlines = [DetalleVentaInline]