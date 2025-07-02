from django.contrib import admin
from .models import Categoria, Producto, Resena

# Register your models here.
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'slug')
    prepopulated_fields = {'slug': ('nombre',)}

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock', 'categoria')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('nombre','categoria')
    prepopulated_fields = {'slug': ('nombre',)}
    
    
@admin.register(Resena)
class ResenaAdmin(admin.ModelAdmin):
    list_display = ('producto', 'autor', 'calificacion', 'creado_en')
    list_filter = ('creado_en','calificacion')
    search_fields = ('autor', 'texto')