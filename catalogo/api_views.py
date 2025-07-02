#from rest_framework.decorators import api_view
from rest_framework import viewsets, permissions
from .models import Producto
from .serializers import ProductoSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    """ 
    Este ViewSet provee `list`, `retrieve`, `create`, `update`,
    `partial_update`, y `destroy`.
    """
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    lookup_field = 'slug' # Usar el slug para buscar en lugar del ID
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# @api_view(['GET'])
# def producto_list_api(request):
#     """ 
#     Una vista que retorna todos los productos en formato JSON.
#     """
#     productos = Producto.objects.all()
#     serializer = ProductoSerializer(productos, many=True, context={'request': request})
#     return Response(serializer.data)


# @api_view(['GET'])
# def producto_detalle_api(request, slug):
#     """ 
#     Una vista que retorna un unico producto basado en su slug.
#     """
#     try:
#         producto = Producto.objects.get(slug=slug)
#         serializer = ProductoSerializer(producto, context={'request': request})
#         return Response(serializer.data)
#     except Producto.DoesNotExist:
#         return Response(status=404, data={'message': 'Producto no encontrado'})