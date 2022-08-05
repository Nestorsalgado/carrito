"""CarritoCompras URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from Carritoladrillos.views import agregar_propiedad, eliminar_propiedad, restar_propiedad, limpiar

from Carritoladrillos.views import tienda

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', tienda, name="Tienda"),
    path('agregar/<int:propiedad_id>',  agregar_propiedad, name='Add'),
    path('eliminar/<int:propiedad_id>', eliminar_propiedad, name='Del'),
    path('restar/<int:propiedad_id>',   restar_propiedad, name='Sub'),
    path('limpiar/',  limpiar, name='Cls'),
   
    
]
