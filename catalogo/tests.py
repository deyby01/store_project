from django.test import TestCase
from django.urls import reverse
from .models import Producto, Categoria

# Create your tests here.
class CatalogoTest(TestCase):
    
    def setUp(self):
        """ 
        Este metodo se ejcuta ANTES de cada prueba.
        Lo usamos para crear objetos que necesitaremos en multiples tests.
        """
        self.categoria = Categoria.objects.create(nombre='Tecnologia')
        self.producto = Producto.objects.create(
            nombre='Laptop Gamer',
            descripcion='Potencia Extrema',
            precio=80.00,
            categoria=self.categoria
        )
        
    def test_modelo_producto(self):
        """
        Prueba que el modelo producto se crea correctamente.
        """
        self.assertEqual(self.producto.nombre, 'Laptop Gamer')
        self.assertEqual(str(self.producto), 'Laptop Gamer')
        self.assertEqual(self.producto.slug, 'laptop-gamer')
        print('✓ Prueba de modelo de producto superada')
        
    def test_vista_home(self):
        """Prueba que la pagina de inicio funciona y usa el template correcto"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalogo/home.html')
        self.assertContains(response, 'Laptop Gamer')
        print('✓ Prueba de vista de inicio superada')
        
    def test_logica_agregar_al_carrito(self):
        """Prueba que podemos agregar un producto al carrito en la sesion."""
        # Usamos self.client para simular la peticion de un usuario
        self.client.post(reverse('agregar_al_carrito', args=[self.producto.id]))
        
        # Verificamos que el carrito de la sesion contiene nuestro producto
        carrito_sesion = self.client.session.get('carrito', {})
        self.assertEqual(len(carrito_sesion), 1)
        self.assertIn(str(self.producto.id), carrito_sesion)
        self.assertEqual(carrito_sesion[str(self.producto.id)], 1)
        print('✓ Prueba de logica del carrito superada')
        