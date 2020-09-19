from django.urls import path
from apps.post.views import PostAgregar, PostListar, MostrarPost


urlpatterns = [
    path('CrearPost/' , PostAgregar.as_view() , name='CrearPost'),
    path('PosteosRecientes/' , PostListar.as_view() , name='PosteosRecientes'),
    path('Post/<int:pk>/', MostrarPost.as_view() , name='MostrarPost'),

]