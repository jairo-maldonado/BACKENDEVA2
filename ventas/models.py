from django.db import models
from django.core.exceptions import ValidationError

class Producto(models.Model):
    nombre = models.CharField(max_length=200, verbose_name="Nombre del Producto")
    precio = models.PositiveIntegerField(verbose_name="Precio (CLP)")
    stock = models.PositiveIntegerField(default=0, verbose_name="Stock Disponible")

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['nombre']

    def __str__(self):
        return f"{self.nombre} - ${self.precio:,}".replace(',', '.')


class Venta(models.Model):
    fecha = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de la Venta")
    cliente = models.CharField(max_length=150, blank=True, null=True, help_text="Opcional")
    total = models.PositiveIntegerField(default=0, verbose_name="Total de la Venta (CLP)")

    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"
        ordering = ['-fecha']

    def __str__(self):
        fecha_formateada = self.fecha.strftime('%d/%m/%Y %H:%M') if self.fecha else "Borrador"
        return f"Venta #{self.id} - {fecha_formateada}"

    def actualizar_total(self):
        self.total = sum(detalle.subtotal for detalle in self.detalles.all())
        super().save(update_fields=['total'])


class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, related_name='detalles', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField(default=1)
    subtotal = models.PositiveIntegerField(default=0, editable=False)

    class Meta:
        verbose_name = "Detalle de Venta"
        verbose_name_plural = "Detalles de Ventas"

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"

    def clean(self):
        if self.producto and self.producto.stock < self.cantidad:
            raise ValidationError(f"No hay suficiente stock para '{self.producto.nombre}'. Stock actual: {self.producto.stock}")

    def save(self, *args, **kwargs):
        self.clean()
        self.subtotal = self.cantidad * self.producto.precio
        
        # Descontar stock si es un registro nuevo
        if not self.pk:
            self.producto.stock -= self.cantidad
            self.producto.save(update_fields=['stock'])

        super().save(*args, **kwargs)
        self.venta.actualizar_total()