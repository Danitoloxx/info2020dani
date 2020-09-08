from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .forms import RegistroUsuarioForm, EditarUsuarioForm
from .models import Usuario



class RegistroUsuario(CreateView):
    model = Usuario
    form_class = RegistroUsuarioForm
    template_name = 'usuarios/registro.html'
    success_url = reverse_lazy('inicio')

class ModificarUsuario(UpdateView):
    model = Usuario
    form_class = EditarUsuarioForm
    template_name = 'usuarios/editar.html'
    success_url = reverse_lazy('perfil')

    def get_object(self):
        return self.request.user