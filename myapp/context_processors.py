from categoria.models import Categoria

def categorias_context(request):
    categorias = Categoria.objects.all()
    return {'categoria': categorias}