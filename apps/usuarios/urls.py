from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as authViews
from django.urls import reverse_lazy
from . import views

app_name="usuarios"

urlpatterns = [
    path('Registrar/', views.RegistroUsuario.as_view(success_url = reverse_lazy('usuarios:registrar_completo')), name = "registrar"),
    path('Registrar/finalizado', views.RegistroUsuario.as_view(template_name="usuarios/registroCompleto.html"), name = "registrar_completo"),
    path('EditarUsuario/', views.ModificarUsuario.as_view(), name = "editar"),
    path('Reset/contrasena-reset/', authViews.PasswordResetView.as_view(template_name ='usuarios/resetPass1.html', email_template_name = 'usuarios/resetPass2.html', success_url = reverse_lazy('usuarios:password_reset_done')), name = "password_reset"),
    path('Reset/contrasena-modificada/',authViews.PasswordResetDoneView.as_view(template_name = 'usuarios/resetPass3.html'), name = "password_reset_done"),
    path('Reset/<uidb64>/<token>/', authViews.PasswordResetConfirmView.as_view(template_name = 'usuarios/resetPass4.html', success_url = reverse_lazy('usuarios:password_reset_complete')), name = "password_reset_confirm"),
    path('Reset/contrasena-lista/', authViews.PasswordResetCompleteView.as_view(template_name = 'usuarios/resetPass5.html'), name = "password_reset_complete"),
]