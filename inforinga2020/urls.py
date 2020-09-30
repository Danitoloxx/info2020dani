from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.Home , name='inicio'),    
    path('Login' , auth.LoginView.as_view(template_name="usuarios/login.html") , name='login'),
    path('Logout' , auth.LogoutView.as_view() , name='logout'),
    path('Perfil', views.Perfil, name='perfil'),

    #Apps incluidas
    path('Usuarios',include('apps.usuarios.urls')),

    # RUTA APP POST
	path('', include('apps.post.urls')), 

	# AGREGO EL MEDIA_URL A LAS URL   
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

