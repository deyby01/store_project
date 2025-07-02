from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import api_views

# 1. Creamos un router
router = DefaultRouter()
# 2. Registramos nuestro ViewSet con el router
router.register(r'productos', api_views.ProductoViewSet, basename='producto')
# 3. Las URLs de la API son ahora generadas automaticamente por el router
urlpatterns = [
    path('', include(router.urls)),
]