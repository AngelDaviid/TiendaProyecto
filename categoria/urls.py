from django.urls import path
from . import views

urlpatterns = [
    path('<int:categoria_id>/',views.categoria_detalles, name='categoria_detalle')
]
