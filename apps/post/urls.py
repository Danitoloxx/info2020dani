from django.urls import path
from apps.post.views import *


urlpatterns = [
    path('Post/Crear/' , PostAgregar.as_view() , name='CrearPost'),
    path('PosteosRecientes/' , PostListar.as_view() , name='PosteosRecientes'),
    path('Post/<int:pk>/', MostrarPost.as_view() , name='MostrarPost'),
    path('Post/Edit/<int:pk>/', PostEditar.as_view() , name='EditarPost'),
    path('Post/Eliminar/<str:pk>', PostEliminar.as_view(), name="EliminarPost"),
    path('Post/Like/<str:pk>', LikeView, name="like_post"),
	path('Post/<int:pk>/Comment/' , ComentarioAgregar.as_view() , name='CrearComentario'),
    path('Buscar/', BuscarPost, name="Buscador"),
]