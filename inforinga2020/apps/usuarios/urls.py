from django.contrib import admin
from django.urls import path
from . import views

app_name="usuarios"

urlpatterns = [
    path('Registrar/', views.RegistroUsuario.as_view(), name = "registrar"),
    path('EditarUsuario/', views.ModificarUsuario.as_view(), name = "editar"),
]