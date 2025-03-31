from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import UsuarioCreateView, UsuarioViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)

urlpatterns = [

    path('', include(router.urls)),
    path('registrar/', UsuarioCreateView.as_view(), name='registrar-usuario'), # Este es el path para registrar un nuevo usuario
]
