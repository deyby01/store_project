from decimal import Decimal
from pyexpat import model
from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Resena
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView
from .forms import ResenaForm


# -------- Vistas basadas en clases (CBV) -----------------------

class HomeView(ListView):
    model = Producto
    template_name = 'catalogo/home.html'
    context_object_name = 'productos'



# ------- Vistas basadas en funciondes (FBV) ----------------------- 

# def home(request):
#     productos = Producto.objects.all()
#     context = {
#         'productos': productos,
#     }
#     return render(request, 'catalogo/home.html', context)


def detalle_producto(request, slug):
    producto = get_object_or_404(Producto, slug=slug)
    resenas = producto.resenas.all()
    
    # Logica del formulario
    if request.method == 'POST':
        form = ResenaForm(request.POST)
        if form.is_valid():
            # No lo guardamos aun para asignar el producto
            nueva_resena = form.save(commit=False)
            nueva_resena.producto = producto
            nueva_resena.save()
            # Redirigimos a la misma pagina para ver la reseña
            return redirect('detalle_producto', slug=producto.slug)
    else:
        form = ResenaForm()
    
    context = {
        'producto': producto,
        'resenas': resenas,
        'form': form
    }
    return render(request, 'catalogo/detalle_producto.html', context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()      
    context = {
        'form': form
    }
    return render(request, 'registration/signup.html', context)


def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    # Obtenemos el carrito de la sesion o creamos uno nuevo si no existe.
    carrito = request.session.get('carrito', {})
    
    # Añadimos o actualizamos la cantidad del producto
    # Usamos el id del producto como string para que sea compatible con JSON
    id_producto_str = str(producto.id)
    cantidad = carrito.get(id_producto_str, 0) + 1
    carrito[id_producto_str] = cantidad
    
    # Guardamos el carrito de nuevo en la sesion
    request.session['carrito'] = carrito
    return redirect('detalle_producto', slug=producto.slug)


def ver_carrito(request):
    carrito = request.session.get('carrito', {})
    productos_en_carrito = []
    total = Decimal('0.00')
    
    for producto_id, cantidad in carrito.items():
        producto = get_object_or_404(Producto, id=int(producto_id))
        subtotal = producto.precio.to_decimal() * cantidad
        productos_en_carrito.append({
            'producto': producto,
            'cantidad': cantidad,
            'subtotal': subtotal
        })
        total += subtotal
    
    contexto = {
        'productos_en_carrito': productos_en_carrito,
        'total': total
    }
    return render(request, 'catalogo/ver_carrito.html', contexto)


def eliminar_del_carrito(request, producto_id):
    carrito = request.session.get('carrito', {})
    id_producto_str = str(producto_id)
    
    if id_producto_str in carrito:
        del carrito[id_producto_str]
        request.session['carrito'] = carrito
        
    return redirect('ver_carrito')