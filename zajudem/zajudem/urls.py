"""
URL configuration for zajudem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apps.users.views import Login, Logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('apps.users.urls')),
    path('fichas/', include('apps.fichas.urls')), # URL para las fichas
    path('aulas/', include('apps.aulas.urls')), # URL para las aulas
    path('inventario/', include('apps.inventario.urls')), # URL para el inventario
    path('programacion/', include('apps.programacion.urls')), # URL para la programación
    path('', Login.as_view(), name='login'), # URL para pruebas de inicio de sesión
    path('logout/', Logout.as_view(), name='logout'), # URL para pruebas de cerrar sesión
]
