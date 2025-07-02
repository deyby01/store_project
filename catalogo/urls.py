from django.urls import path
from .views import HomeView, detalle_producto, register, ver_carrito, agregar_al_carrito, eliminar_del_carrito

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('producto/<slug:slug>/', detalle_producto, name='detalle_producto'),
    path('register/', register, name='register'),
    path('add/<int:producto_id>/', agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/', ver_carrito, name='ver_carrito'),
    path('eliminar/<int:producto_id>/', eliminar_del_carrito, name='eliminar_del_carrito'),
]
