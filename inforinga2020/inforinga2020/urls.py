from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.Home , name='inicio'),    
    path('Login' , auth.LoginView.as_view(template_name="usuarios/login.html") , name='login'),
    path('Logout' , auth.LogoutView.as_view() , name='logout'),
    path('Usuarios',include('apps.usuarios.urls'))
]
