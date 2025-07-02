from rest_framework import serializers
from .models import Producto, Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre', 'slug']
        
        
class ProductoSerializer(serializers.ModelSerializer):
    # Para mostrar el nombre de la categoria en lugar de su ID
    categoria = serializers.StringRelatedField()
    url = serializers.HyperlinkedIdentityField(
        view_name='producto-detail',
        lookup_field='slug'
    )
    
    class Meta:
        model = Producto
        fields = ['id', 'url', 'nombre', 'descripcion', 'precio', 'stock', 'categoria', 'slug']
        