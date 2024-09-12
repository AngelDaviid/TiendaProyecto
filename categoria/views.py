from django.shortcuts import render, get_object_or_404
from .models import Categoria

# Create your views here.

def categorias(request):
    categorias = Categoria.objects.all()
    return{'categorias': categorias}

def categoria_detalles(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    return render(request, 'categoria/categoria_detalles.html', {'categoria': categoria})

    