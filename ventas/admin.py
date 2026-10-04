from django.contrib import admin
from .models import Producto, Venta, DetalleVenta

admin.site.site_header = "Administración de Ventas - Mi Tienda"
admin.site.site_title = "Portal de Ventas"
admin.site.index_title = "Panel de Control Principal"

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock')
    search_fields = ('nombre',)
    list_filter = ('stock',)

class DetalleVentaInline(admin.TabularInline):
    model = DetalleVenta
    extra = 1
    readonly_fields = ('subtotal',)

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha', 'cliente', 'total')
    list_filter = ('fecha',) 
    date_hierarchy = 'fecha' 
    search_fields = ('cliente',)
    readonly_fields = ('total',)
    inlines = [DetalleVentaInline]

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for obj in formset.deleted_objects:
            obj.delete()
        for instance in instances:
            instance.save()
        formset.save_m2m()
        
        venta = form.instance
        total_calculado = sum(detalle.subtotal for detalle in venta.detalles.all())
        venta.total = total_calculado
        venta.save()