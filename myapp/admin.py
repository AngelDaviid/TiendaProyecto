from django.contrib import admin
from carrito.models import Carrito, ItemCarrito
from myapp.models import Producto
from clientes.models import Cliente
from Pedidos.models import Pedido, ItemPedido
from categoria.models import Categoria



admin.site.register(Cliente)
admin.site.register(ItemCarrito)
admin.site.register(ItemPedido)
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Pedido)
admin.site.register(Carrito)

# Register your models here.
