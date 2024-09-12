from django.urls import path
from . import views

urlpatterns = [
    path('<int:categoria_id>/',views.categoria_detalles, name='categoria_detalle'),
    path('<int:productos_id>/',views.categoria_productos, name='categoria_productos'),
]
