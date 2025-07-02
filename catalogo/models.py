from django.db import models
from django.utils.text import slugify

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    
    # hacemos que el slug se genere automaticamente con el titulo
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre
    

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    slug = models.SlugField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre
    
    
class Resena(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='resenas')
    autor = models.CharField(max_length=100)
    texto = models.TextField()
    # Este campo podria no existir en todos los documentos
    calificacion = models.IntegerField(null=True, blank=True)
    
    creado_en = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Reseña de {self.autor} para {self.producto.nombre}'