from django.urls import path
from .views import (
    ProductoListView,
    ProductoCreateView,
    ProductoUpdateView,
    ProductoDeleteView
)

app_name = 'ventas'

urlpatterns = [
    path('', ProductoListView.as_view(), name='listar_productos'),
    path('crear/', ProductoCreateView.as_view(), name='crear_producto'),
    path('editar/<int:pk>/', ProductoUpdateView.as_view(), name='editar_producto'),
    path('eliminar/<int:pk>/', ProductoDeleteView.as_view(), name='eliminar_producto'),
]